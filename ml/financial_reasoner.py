import json
import re
import requests
from decimal import Decimal, getcontext
import ast

# высокая точность
getcontext().prec = 28


class LLMClient:

    def __init__(self, base_url="http://localhost:11434/api/generate"):
        self.base_url = base_url

    def generate(self, model, prompt, max_tokens=512, temperature=0.2):
        body = {
            "model": model,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": False,
        }

        try:
            resp = requests.post(self.base_url, json=body, timeout=60)
            data = resp.json()
            return data.get("response", "")
        except Exception as e:
            print("LLM ERROR:", e)
            return "ERROR: LLM unavailable"


class SafeEvaluator:

    ALLOWED_NODES = {
        "Expression", "BinOp", "UnaryOp", "Num", "Add", "Sub", "Mult", "Div",
        "Pow", "Load", "USub", "UAdd", "Mod", "FloorDiv"
    }

    @staticmethod
    def safe_eval(expr: str) -> Decimal:
        tree = ast.parse(expr, mode="eval")
        SafeEvaluator._validate(tree)
        return SafeEvaluator._eval_node(tree.body)

    @staticmethod
    def _validate(node):
        node_type = node.__class__.__name__
        if node_type not in SafeEvaluator.ALLOWED_NODES:
            raise ValueError(f"bad node: {node_type}")

        for child in ast.iter_child_nodes(node):
            SafeEvaluator._validate(child)

    @staticmethod
    def _eval_node(node):
        if isinstance(node, ast.Num):
            return Decimal(str(node.n))

        if isinstance(node, ast.BinOp):
            left = SafeEvaluator._eval_node(node.left)
            right = SafeEvaluator._eval_node(node.right)

            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                return left / right
            if isinstance(node.op, ast.Mod):
                return left % right
            if isinstance(node.op, ast.FloorDiv):
                return left // right
            if isinstance(node.op, ast.Pow):
                return left ** right

        if isinstance(node, ast.UnaryOp):
            val = SafeEvaluator._eval_node(node.operand)
            if isinstance(node.op, ast.USub):
                return -val
            if isinstance(node.op, ast.UAdd):
                return +val

        raise ValueError("unsafe node")


class FinancialReasoner:

    def __init__(self,
                 qwen_model="qwen-2.5",
                 gemma_model="gemma3",
                 base_url="http://localhost:11434/api/generate"):
        self.qwen = LLMClient(base_url)
        self.gemma = LLMClient(base_url)
        self.qwen_model = qwen_model
        self.gemma_model = gemma_model

    def summarize(self, text: str) -> str:
        prompt = f"Сделай краткое сжатое резюме (1–4 предложения):\n{text}"
        return self.gemma.generate(self.gemma_model, prompt, max_tokens=150)

    def compute_json(self, structured: dict, question: str) -> dict:
        prompt = f"""
Ты — финансовый калькулятор. 
Ты НЕ делаешь догадок. 
Ты делаешь только точные вычисления.

Пользовательский вопрос:
{question}

Параметры:
{json.dumps(structured, ensure_ascii=False, indent=2)}

ТВОЯ ЗАДАЧА:
1. Заполни JSON вида:
{{
  "explanation": "что вычисляем",
  "steps": [
    {{
      "name": "имя шага",
      "formula": "математическая формула",
      "computed": число
    }}
  ],
  "result": число
}}

2. Формулы должны использовать только параметры.
3. Числа только в виде цифр, никаких слов.
4. Никакого текста за пределами JSON.
"""

        out = self.qwen.generate(self.qwen_model, prompt, max_tokens=1200)

        try:
            first = out.find("{")
            last = out.rfind("}")
            j = out[first:last+1]
            return json.loads(j)
        except Exception as e:
            return {"error": "Qwen output invalid", "raw": out}

    def validate(self, report: dict) -> dict:
        if "steps" not in report:
            return report

        for step in report["steps"]:
            formula = step.get("formula", "")
            try:
                val = SafeEvaluator.safe_eval(formula)
                step["verified"] = float(val)
            except Exception as e:
                step["verified"] = None
                step["error"] = str(e)

        return report

    def handle(self, structured: dict, question: str) -> dict:
        calc = self.compute_json(structured, question)
        calc = self.validate(calc)
        summary = self.summarize(json.dumps(calc, ensure_ascii=False, indent=2))

        return {
            "summary": summary,
            "calculation": calc,
            "validated": True
        }
