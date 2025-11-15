from sentence_transformers import SentenceTransformer
from db.scripts.operations_db import save_vectors
import numpy as np

CATEGORIES = []

model = SentenceTransformer(
    'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')


def embed(chunks):
    embeddings = model.encode(chunks)

    return embeddings.tolist()


def find_similarities(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * (np.linalg.norm(vec2)))


def find_breakpoints(similarities, percentile=10):
    embed_similarities = [similarity[0] for similarity in similarities]
    threshold_value = np.percentile(embed_similarities, percentile)
    print(f'Порог отсечения: {threshold_value:.2f}')

    return [i for i, sim in enumerate(similarities) if sim[0] < threshold_value and sim[1]]


def chunking(sentences, breakpoints):
    chunks = []
    start = 0
    text = []
    for sentence in sentences:
        text.append(sentence[0])

    for bp in breakpoints:
        chunks.append(". ".join(text[start:bp + 1]) + '.')
        CATEGORIES.append(sentences[start][1])
        start = bp + 1
    chunks.append(". ".join(text[start:]))
    CATEGORIES.append(sentences[start][1])

    return chunks


financial_file = open('base_texts/financial_text.txt', 'r', encoding='utf-8')
hr_file = open('base_texts/hr_text.txt', 'r', encoding='utf-8')
law_file = open('base_texts/law_text.txt', 'r', encoding='utf-8')
marketing_file = open('base_texts/marketing_text.txt', 'r', encoding='utf-8')

print(1)
sentences_lst = [(sentence, 'финансы') for sentence in
    financial_file.readline().split('. ')] + [(sentence, 'найм') for sentence in
    hr_file.readline().split('. ')] + [(sentence, 'юриспруденция') for sentence in
    law_file.readline().split('. ')] + [(sentence, 'маркетинг') for sentence in
    marketing_file.readline().split('. ')]

financial_file.close()
hr_file.close()
law_file.close()
marketing_file.close()

sentences_embeddings = [(embed(sentence[0]), sentence[1]) for sentence in
                        sentences_lst]

similarities_lst = [
    (find_similarities(sentences_embeddings[i][0], sentences_embeddings[i + 1][0]),
     sentences_embeddings[i][1] == sentences_embeddings[i + 1][1])
    for i in range(len(sentences_lst) - 1)
]

print(2)
breakpoints_lst = find_breakpoints(similarities_lst,
                                   percentile=10)  # отсечение 10 процентов низкого сходства

semantic_chunks = chunking(sentences_lst, breakpoints_lst)
chunk_embeddings = [embed(chunk) for chunk in semantic_chunks]

print(3)
print(save_vectors(semantic_chunks, chunk_embeddings, CATEGORIES))

