from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
summarizer = pipeline("summarization", model="t5-small")

class SummarizeRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(request: SummarizeRequest):
    summary = summarizer(request.text, max_length=140, min_length=30, do_sample=False)
    return {"summary": summary[0]["summary_text"]}
