from conn import fetch_data
from pinecone_setup import initialize_pinecone, upsert_to_pinecone, query_pinecone
from sentence_transformer import generate_embeddings, generate_embedding


def sim_check(user_query):
    data = fetch_data()
    embeddings = generate_embeddings(data)

    index = initialize_pinecone("api_key", "us-west1-gcp", "name", dimension=384)

    upsert_to_pinecone(index, embeddings)

    query_embedding = generate_embedding(user_query).tolist()

    results = query_pinecone(index, query_embedding)
    return results