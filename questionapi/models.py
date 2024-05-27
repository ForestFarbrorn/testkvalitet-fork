class Question():
    def __init__(self, qid: int, question_text: str, answer_text: str) -> None:
        self.qid = qid
        self.question_text = question_text
        self.answer_text = answer_text

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Question):
            return False

        return self.qid == o.qid and self.question_text == o.question_text and self.answer_text == o.answer_text