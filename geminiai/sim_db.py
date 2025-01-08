from conn import mysqlConnect
from pinecone_setup import pineconeHandler
from sentence_transformer import embeddingGenerator
import config

class simmilarity_check:
    def __init__(self, api_key=None, region=None, index_name=None, dimension=None):
        self.api_key = api_key or config.pinecone_api_key
        self.region = region or config.pinecone_region
        self.index_name = index_name or config.pinecone_index_name
        self.dimension = dimension or config.pinecone_dimension
        self.index = self._initialize_pinecone()

    def _initialize_pinecone(self):
        return pineconeHandler(self.api_key, self.region, self.index_name, self.dimension)
    
    def prepare_index(self):
        db_connection = mysqlConnect()
        db_connection.connect()
        data1,_ = db_connection.fetch_data()
        db_connection.closeConn()

        embed_gen = embeddingGenerator()
        embeddings = embed_gen.generate_embeddings(data1)

        self.index.upsert(embeddings)

    def check_similarity(self, user_query):

        embed_gen = embeddingGenerator()
        query_embedding = embed_gen.generate_embedding(user_query).tolist()
        results = self.index.query(query_embedding, top_k=1)
        return results