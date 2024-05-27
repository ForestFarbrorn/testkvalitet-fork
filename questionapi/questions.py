from pydantic import BaseModel
from questionapi.db import QuestionDB
from questionapi.models import Question
from fastapi import FastAPI

db = QuestionDB()
db.initialize_db()

app = FastAPI()

class QuestionCreate(BaseModel):
    question_text: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/questions/", status_code=201)
def add_question(question: QuestionCreate):
    """Adds a new question"""

    new_question = Question(qid=0, question_text=question.question_text, answer_text="")

    db.add_question(question=new_question)

    return new_question

def get_question(qid):
    """Gets a question for a given id"""

    return db.get_question(qid)

def get_all_questions():
    """Returns all the questions in the database."""
    
    return db.get_all_questions()