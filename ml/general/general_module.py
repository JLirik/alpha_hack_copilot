import datetime
from config import *
from ollama import Client


ollama_client = Client()


def generate(prompt: str, city='Нет данных, игнорируй', business_info='Нет данных, игнорируй') -> str:
    user_prompt = prompt
    prompt = str(open('prompts/generate_prompt.txt', encoding="utf-8").read())
    prompt = prompt.replace('city', city).replace('business_info', business_info)
    prompt = prompt.replace('question', user_prompt)
    response = ollama_client.chat(model=MODEL, messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']


if __name__ == '__main__':
    print('Запуск ручного режима тестирования модуля')
    _prompt = input('Введите запрос: ')
    start = datetime.datetime.now()
    print(f'Генерация ответа...')
    print(generate(_prompt))
    print(f'\nГотово! Ответ занял {datetime.datetime.now() - start}')