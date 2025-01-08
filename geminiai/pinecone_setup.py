from pinecone import Pinecone
import config

class pineconeHandler:
    def __init__(self, api_key=None, environment=None, index_name=None, dimension=None):
        self.api_key = api_key or config.pinecone_api_key
        self.environment = environment or config.pinecone_region
        self.index_name = index_name or config.pinecone_index_name
        self.dimension = dimension or config.pinecone_dimension
        self.pinecone_client = Pinecone(api_key=self.api_key)
        self.index = self.pinecone_client.Index(config.pinecone_index_name, config.pinecone_index_host)

    def upsert(self, embeddings, batch_size=100):
        for i in range(0, len(embeddings), batch_size):
            batch = embeddings[i : i + batch_size]
            self.index.upsert(vectors=batch)

    def query(self, vector, top_k=1):
        return self.index.query(vector=vector, top_k=top_k, include_metadata=False)