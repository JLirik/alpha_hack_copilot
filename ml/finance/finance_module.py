import datetime
from config import *
from ollama import *


ollama_client = Client()


def calculate_problem(user_prompt):
    prompt = str(open('prompts/calculation_prompt.txt', encoding="utf-8").read())
    prompt = prompt.replace('question', user_prompt, 1)
    response = ollama_client.chat(model=CALCULATION_MODEL, messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']


def explain_solution(problem, solution):
    if '{' in solution:
        prompt = str(open('prompts/explanation_prompt.txt', encoding="utf-8").read())
        prompt = prompt.replace('problem', problem).replace('solution', solution)
        response = ollama_client.chat(model=EXPLANATION_MODEL, messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']
    else:
        return solution


def generate(prompt: str) -> str:
    problem_solution = calculate_problem(prompt)
    result = explain_solution(prompt, problem_solution)
    return result


if __name__ == '__main__':
    print('Запуск ручного режима тестирования модуля')
    _prompt = input('Введите запрос: ')
    start = datetime.datetime.now()
    print(f'Генерация ответа...')
    print(generate(_prompt))
    print(f'\nГотово! Ответ занял {datetime.datetime.now() - start}')