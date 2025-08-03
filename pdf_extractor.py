from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
            return text
    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {str(e)}")

def chunk_text(text,chunk_size=500):
    sentences=text.split('\n')
    chunks = []
    current_chunk=""
    for sentence in sentences:
        if len(current_chunk)+len(sentence)<chunk_size:
            current_chunk+=sentence+" "
        else:
            chunks.append(current_chunk.strip())
            current_chunk=sentence+" "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def create_embeddings(chunks, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks)
    index=faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return model,index,chunks

def save_data(model, index, chunks):
    faiss.write_index(index, "ideanest_index.faiss")
    with open("ideanest_chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)
    model.save("ideanest_embeddings_model")
pdf_path = "IdeaNestTech_Chatbot_Info.pdf"
pdf_content = extract_text_from_pdf(pdf_path)
chunks = chunk_text(pdf_content)
model,index,chunks=create_embeddings(chunks)
save_data(model, index, chunks)
print(f"{len(chunks)} chunks created and embeddings indexed!")