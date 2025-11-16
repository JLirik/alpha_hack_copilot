import datetime
import json
from ollama import Client
from config import *


ollama_client = Client()


def generate_answer(user_prompt, _city, _business_info, liked_post_text):
    def is_valid_json(json_text):
        try:
            json.loads(json_text)
            return True
        except json.JSONDecodeError:
            return False
    while True:
        if liked_post_text is None:
            prompt = open('prompts/first_posts_generation_prompt.txt', encoding="utf-8").read()
        else:
            prompt = open('prompts/generate_simular_prompt.txt', encoding="utf-8").read()
        prompt = prompt.replace('text', user_prompt)
        prompt = prompt.replace('city', _city).replace('business_info', _business_info)
        response = ollama_client.chat(model=GENERATION_MODEL, messages=[{'role': 'user', 'content': prompt}])
        if is_valid_json(response['message']['content']) or '{' not in response['message']['content']:
            break
        else:
            print(f'{GENERATION_MODEL} дала не валидный json, переделываем:\n\n{response['message']['content']}')
    return response['message']['content']


def generate(prompt: str, _city='Нет данных, игнорируй', _business_info='Нет данных, игнорируй', liked_post_text=None):
    result = generate_answer(prompt, _city, _business_info, liked_post_text)
    return result


if __name__ == '__main__':
    print('Запуск ручного режима тестирования модуля')
    _prompt = input('Введите запрос: ')
    start = datetime.datetime.now()
    print(f'Генерация ответа...')
    print(generate(_prompt))
    print(f'\nГотово! Ответ занял {datetime.datetime.now() - start}')
