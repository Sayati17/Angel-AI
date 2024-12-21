from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
model = model.to('cuda')

def generate_embeddings(data, batch_size=32):
    ids = [str(row[0]) for row in data]
    texts = [row[1] for row in data]
    embeddings = []
    
    for i in range(0, len(texts), batch_size):
        batch_embeddings = model.encode(texts[i:i + batch_size], batch_size=batch_size, device='cuda')
        embeddings.extend(batch_embeddings)
    
    return list(zip(ids, embeddings))

def generate_embedding(text):
  return model.encode(text, device='cuda')