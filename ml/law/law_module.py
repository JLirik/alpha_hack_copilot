import datetime
import find_article
from config import *
from ollama import Client


ollama_client = Client()


def get_context(prompt):
    documents = find_article.retrieve_law(prompt)
    joined_documents = []
    for doc in documents:
        joined_doc = '\n'.join(doc)
        joined_documents.append(joined_doc)
    context = '\n'.join(joined_documents)
    return context


def generate(prompt: str, city: str, business_info: str) -> str:
    context = get_context(prompt)
    user_prompt = prompt
    prompt = str(open('prompts/generation_prompt.txt', encoding="utf-8").read())
    prompt = prompt.replace('question', user_prompt).replace('context', context)
    prompt = prompt.replace('city', city).replace('business_info', business_info)
    response = ollama_client.chat(model=MODEL, messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']


if __name__ == '__main__':
    print('Запуск ручного режима тестирования модуля')
    _prompt = input('Введите запрос: ')
    start = datetime.datetime.now()
    print(f'Генерация ответа...')
    print(generate(_prompt))
    print(f'\nГотово! Ответ занял {datetime.datetime.now() - start}')