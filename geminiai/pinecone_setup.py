from pinecone import Pinecone

def initialize_pinecone(api_key, environment, index_name, dimension):
    pc = Pinecone(api_key=api_key)
    index = pc.Index("angelai", "https://angelai-bbnnx1q.svc.aped-4627-b74a.pinecone.io")
    return index

def upsert_to_pinecone(index, embeddings, batch_size=100):
    for i in range(0, len(embeddings), batch_size):
        batch = embeddings[i : i + batch_size]
        index.upsert(vectors=batch)

def query_pinecone(index, vector, top_k=1):
    return index.query(vector=vector, top_k=top_k, include_metadata=False)