
from questions import add_question, db

def test_add_question_adds_question_to_db():
    new_question = add_question("New question")

    assert db.get_question(new_question.qid) == new_question