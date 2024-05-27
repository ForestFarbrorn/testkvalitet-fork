from unittest.mock import MagicMock
from questions import Question, add_question
from db import QuestionDB

def test_add_question_returns_question_obj():
    new_question = add_question('Sample question')

    assert isinstance(new_question, Question)
    assert new_question.question_text == 'Sample question'

def test_add_question_calls_db(mocker):
    mock_db_instance = mocker.patch.object(QuestionDB, 'add_question')

    add_question('Test question')

    mock_db_instance.assert_called_once()

