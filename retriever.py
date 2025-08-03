from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np

def load_assets():
    index=faiss.read_index("ideanest_index.faiss")
    with open("ideanest_chunks.pkl", "rb") as f:
        chunks=pickle.load(f)
    model = SentenceTransformer("ideanest_embeddings_model")
    return model,index,chunks

def retrieve(query, model, index, chunks, top_k=5):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    return [chunks[i] for i in indices[0]]


if __name__ == "__main__":
    model, index, chunks = load_assets()

    user_query = "Do you offer courses?"
    top_chunks = retrieve(user_query, model, index, chunks)

    print("Top Relevant Chunks:")
    for i, chunk in enumerate(top_chunks):
        print(f"\nChunk {i + 1}:\n{chunk}\n")
