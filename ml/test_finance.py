from ml.finance.financial_reasoner import FinancialReasoner

engine = FinancialReasoner()

print("Введите вопрос:")
q = input("> ")

print("Введите параметры JSON (например {\"price\":300,\"cost\":150}):")
import json
params = json.loads(input("> "))

out = engine.handle(params, q)
print(json.dumps(out, ensure_ascii=False, indent=2))
