from sentence_transformers import SentenceTransformer

class embeddingGenerator:
    def __init__(self, model_name='all-MiniLM-L6-v2', device='cuda'):
        self.model_name = model_name
        self.device = device
        self.model = SentenceTransformer(self.model_name).to(self.device)

    def generate_embeddings(self, data, batch_size=32):
        ids = [str(row[0]) for row in data]
        texts = [row[1] for row in data]
        embeddings = []
        for i in range(0, len(texts), batch_size):
            batch_embeddings = self.model.encode(texts[i:i + batch_size], batch_size=batch_size, device='cuda')
            embeddings.extend(batch_embeddings)
    
        return list(zip(ids, embeddings))
    
    def generate_embedding(self, text):
        return self.model.encode(text, device=self.device)

