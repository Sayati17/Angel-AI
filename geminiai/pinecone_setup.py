from pinecone import Pinecone
import config

class pineconeHandler:
    def __init__(self, api_key, environment, index_name, dimension):
        self.api_key = api_key
        self.environment = environment
        self.index_name = index_name
        self.dimension = dimension
        self.pinecone_client = Pinecone(api_key=self.api_key)
        self.index = self.pinecone_client.Index(config.pinecone_index_name, config.pinecone_index_host)

    def upsert(self, embeddings, batch_size=100):
        for i in range(0, len(embeddings), batch_size):
            batch = embeddings[i : i + batch_size]
            self.index.upsert(vectors=batch)

    def query(self, vector, top_k=1):
        return self.index.query(vector=vector, top_k=top_k, include_metadata=False)