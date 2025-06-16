from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
summarizer = pipeline("summarization", model="sshleifer/tiny-t5")

class SummarizeRequest(BaseModel):
    text: str

class SummarizeResponse(BaseModel):
    summary: str

@app.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    result = summarizer(req.text, max_length=140, min_length=30, do_sample=False)
    return SummarizeResponse(summary=result[0]["summary_text"])
