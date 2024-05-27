from fastapi.testclient import TestClient
from questions import app, db

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_add_question():
    response = client.post("/questions/", json={"question_text": "New question"})
    assert response.status_code == 201
    assert response.json() == {"qid": 1, "question_text": "New question", "answer_text": ""}