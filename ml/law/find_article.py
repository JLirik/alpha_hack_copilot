from sentence_transformers import SentenceTransformer
from db.scripts.operations_db import find_law

model = SentenceTransformer(
    'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

def embed(chunks):
    embeddings = model.encode(chunks)

    return embeddings.tolist()


def retrieve_law(user_request):
    request_embedding = embed(user_request)
    retrieve = find_law(request_embedding)
    return retrieve
