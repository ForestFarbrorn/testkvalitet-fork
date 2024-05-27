from unittest.mock import MagicMock
from questionapi.questions import Question, QuestionCreate, add_question, get_all_questions, get_question
from questionapi.db import QuestionDB

def test_add_question_returns_question_obj(mocker):
    mock_db_instance = mocker.patch.object(QuestionDB, 'add_question')

    new_question = add_question(QuestionCreate(question_text='Sample question'))

    assert isinstance(new_question, Question)
    assert new_question.question_text == 'Sample question'


def test_add_question_calls_db(mocker):
    mock_db_instance = mocker.patch.object(QuestionDB, 'add_question')

    add_question(QuestionCreate(question_text='Test question'))

    mock_db_instance.assert_called_once()

def test_get_question_calls_db(mocker):
    mock_db_instance = mocker.patch.object(QuestionDB, 'get_question')

    get_question(0)

    mock_db_instance.assert_called_once_with(0)


def test_get_all_questions_returns_list(mocker):
    mock_db_instance = mocker.patch.object(
        QuestionDB, 
        'get_all_questions', 
        return_value=[Question(qid=0, question_text='Test question', answer_text='Test answer')]
    )

    questions = get_all_questions()

    assert isinstance(questions, list)
    assert len(questions) == 1
    assert questions[0].question_text == 'Test question'
    assert questions[0].answer_text == 'Test answer'
    mock_db_instance.assert_called_once()