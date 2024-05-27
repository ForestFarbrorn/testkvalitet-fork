from db import db
from models import Question

def add_question(question_text: str):
    """Adds a new question"""

    question = Question(qid=0, question_text=question_text, answer_text="")

    db.add_question(question=question)

    return question

def get_question(qid):
    """Gets a question for a given id"""
    pass

def get_all_questions():
    """Returns all the questions in the database."""
    pass
