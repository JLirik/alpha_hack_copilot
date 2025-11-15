from sentence_transformers import SentenceTransformer
from db.scripts.operations_db import comparing_embeddings
model = SentenceTransformer(
    'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

def embed(chunks):
    embeddings = model.encode(chunks)

    return embeddings.tolist()


def retrieve_context(user_request):
    request_embedding = embed(user_request)
    categories = comparing_embeddings(request_embedding)

    return categories