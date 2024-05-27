from db import QuestionDB

db = QuestionDB()

class Question():
    def __init__(self, qid: int, question_text: str, answer_text: str) -> None:
        self.qid = qid
        self.question_text = question_text
        self.answer_text = answer_text

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
