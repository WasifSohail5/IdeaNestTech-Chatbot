from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from retriever import load_assets,retrieve
from api_integration import init_gemini, build_prompt, ask_gemini

class QuestionRequest(BaseModel):
    question: str
    api_key: str
class AnswerResponse(BaseModel):
    answer: str

app=FastAPI(title="IdeaNestTEch Chatbot")
embed_model,index,chunks=load_assets()

@app.post("/chat",response_model=AnswerResponse)
def chat_with_bot(request: QuestionRequest):
    try:
        model=init_gemini(request.api_key)
        context_chunks = retrieve(request.question, embed_model, index, chunks)
        context="\n\n".join(context_chunks)
        prompt = build_prompt(context, request.question)
        answer=ask_gemini(model,prompt)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
