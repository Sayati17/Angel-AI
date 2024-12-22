from conn import fetch_data
from pinecone_setup import initialize_pinecone, upsert_to_pinecone, query_pinecone
from sentence_transformer import generate_embeddings, generate_embedding
import config

def sim_check(user_query):
    # data1, _ = fetch_data() (uncomment if pinecone does not have vector data, uncomment if pinecone index is new)

    # embeddings = generate_embeddings(data1) (uncomment if pinecone does not have vector data, uncomment if pinecone index is new)

    index = initialize_pinecone(config.pinecone_api, config.pinecone_region, config.pinecone_db, dimension=config.pinecone_dimenstion)

    # upsert_to_pinecone(index, embeddings) (uncomment if pinecone does not have vector data, uncomment if pinecone index is new)

    query_embedding = generate_embedding(user_query).tolist()

    results = query_pinecone(index, query_embedding)
    return results