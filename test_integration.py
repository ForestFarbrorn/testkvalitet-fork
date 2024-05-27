
from questions import add_question, db

def test_add_question_adds_question_to_db():
    add_question("New question")

    assert db.get_question(0)