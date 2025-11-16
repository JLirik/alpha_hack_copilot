from sentence_transformers import SentenceTransformer
from db.scripts.operations_db import comparing_embeddings

model = SentenceTransformer(
    'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

def embed(chunks):
    embeddings = model.encode(chunks)

    return embeddings.tolist()


def retrieve_context(user_request):
    request_embedding = embed(user_request)
    retrieve = comparing_embeddings(request_embedding)
    categories = {'юриспруденция': 0, 'маркетинг': 0, 'финансы': 0, 'найм': 0}
    for e in retrieve:
        categories[e[0]] += (1 - e[1])
    category = max(categories, key=lambda x: categories[x])
    # print(retrieve)

    print(categories, retrieve)

    return category
