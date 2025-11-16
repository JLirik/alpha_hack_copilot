from sentence_transformers import SentenceTransformer
from db.scripts.operations_db import save_vectors
import numpy as np

CATEGORIES = []

model = SentenceTransformer(
    'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')


def embed(chunks):
    embeddings = model.encode(chunks)

    return embeddings.tolist()


financial_file = open('base_texts/financial_text.txt', 'r', encoding='utf-8')
hr_file = open('base_texts/hr_text.txt', 'r', encoding='utf-8')
law_file = open('base_texts/law_text.txt', 'r', encoding='utf-8')
marketing_file = open('base_texts/marketing_text.txt', 'r', encoding='utf-8')

sentences_lst = financial_file.readlines() + hr_file.readlines() + law_file.readlines() + marketing_file.readlines()

financial_file.close()
hr_file.close()
law_file.close()
marketing_file.close()

sentences_lst = [sentence.rstrip() for sentence in sentences_lst]
sentences_embeddings = embed(sentences_lst)

print(save_vectors(sentences_lst[0:15], sentences_embeddings[0:15], 'финансы'))
print(save_vectors(sentences_lst[15:23], sentences_embeddings[15:23], 'найм'))
print(save_vectors(sentences_lst[23:38], sentences_embeddings[23:38], 'юриспруденция'))
print(save_vectors(sentences_lst[38:], sentences_embeddings[38:], 'маркетинг'))

