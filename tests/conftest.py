import pytest
from questionapi.questions import db

@pytest.fixture(autouse=True, scope='function')
def test_db(tmp_path):
    db.filename = tmp_path / 'test.db'
    db.initialize_db()

    yield
    
    # os.remove('test.db')