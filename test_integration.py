import os.path
from questions import QuestionCreate, add_question, db
from pytest import fixture

def test_add_question_adds_question_to_db(test_db):
    new_question = QuestionCreate(question_text="New question")

    added_question = add_question(new_question)

    assert db.get_question(added_question.qid) == added_question