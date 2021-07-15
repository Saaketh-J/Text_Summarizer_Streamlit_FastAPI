from model import generate_summary
from copy import deepcopy
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from enum import Enum


class UserRequestIn(BaseModel):
    text: str
    num_sentences: int


class ResponseOut(BaseModel):
    summarized_text: str


app = FastAPI()


@app.post("/summary", response_model=ResponseOut)
# forces input validation by using Pydantic
def get_summary(user_request: UserRequestIn):
    text = user_request.text
    num_sentences = user_request.num_sentences

    summary = generate_summary(text, num_sentences)

    return {"summarized_text": summary}


@app.get("/")
def hello():
    return {"message": "Hit /docs for documentation"}
