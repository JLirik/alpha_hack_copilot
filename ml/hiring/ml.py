import datetime
import re
import json

from ollama import Client
from ml_config import *
from conversions import *


ollama_client = Client()


def extract_entities(_text):
    _prompt = str(open('prompts/extract_info_prompt.txt', encoding="utf-8").read()).replace('text', _text)
    while True:
        response = ollama_client.chat(model=INFO_EXTRACTION_MODEL, messages=[{'role': 'user', 'content': _prompt}])
        try:
            city, role = response['message']['content'][1:-1].split('|')
            break
        except ValueError:
            print(f'{INFO_EXTRACTION_MODEL} дала кринж ответ, генерируем заново')
    for conv in city_conversions.keys():
        if city.lower() == conv:
            city = city_conversions[conv]
    city = None if city == 'нет' else city
    role = None if role == 'нет' else role
    return city, role


def extract_salary(_text):
    pattern = r'(\d[\d\s.,]*)\s*(?:₽|руб|р|тыс|k|к)'
    match = re.search(pattern, _text.lower())
    if match:
        value = match.group(1)
        value = re.sub(r'\D', '', value)
        value = int(value)
        if value < 1000:
            value *= 1000
        return value
    return None


def extract_employment_type(_text):
    _text = _text.lower()
    if 'удал' in _text:
        return "remote"
    if 'неполн' in _text or 'част' in _text:
        return 'part-time'
    if 'полн' in _text:
        return 'full-time'
    return None


def extract_vacancy_info(_text):
    salary = extract_salary(_text)
    employment_type = extract_employment_type(_text)
    city, role = extract_entities(_text)
    result = {
        'role': role,
        'salary_min': salary,
        'city': city,
        'employment_type': employment_type
    }
    return result


def generate_vacancy(_vacancy_info, _text):
    def is_valid_json(json_text):
        try:
            json.loads(json_text)
            return True
        except json.JSONDecodeError:
            return False
    while True:
        _prompt = open('prompts/generate_vacancy_prompt.txt', encoding="utf-8").read()
        _prompt = _prompt.replace('vacancy', str(_vacancy_info)).replace('text', _text)
        response = ollama_client.chat(model=VACANCY_GENERATION_MODEL, messages=[{'role': 'user', 'content': _prompt}])
        if is_valid_json:
            break
        else:
            print(f'{VACANCY_GENERATION_MODEL} кринжанул с json, переделываем')
    return response['message']['content']


if __name__ == '__main__':
    print('Запуск ручного режима тестирования модуля')
    prompt = input('Введите запрос: ')
    start = datetime.datetime.now()
    # prompt = 'Кондитерская "Сахарные Горы" в Екб ищет слесаря на полный день, зп конфетами'
    print('Извлечение основной информации из запроса...')
    vacancy_info = extract_vacancy_info(prompt)
    print(f'Информация из запроса извлечена. Прошло: {datetime.datetime.now() - start}. Генерация текста вакансии...')
    print(generate_vacancy(vacancy_info, prompt))
    print(f'Готово! Ответ занял {datetime.datetime.now() - start}')
