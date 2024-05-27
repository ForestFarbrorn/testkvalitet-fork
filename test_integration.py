import os.path
from questions import add_question, db
from pytest import fixture

@fixture
def test_db(tmp_path):
    db.filename = tmp_path / 'test.db'
    db.initialize_db()

    yield
    
    # os.remove('test.db')

def test_add_question_adds_question_to_db(test_db):
    new_question = add_question("New question")

    assert db.get_question(new_question.qid) == new_question