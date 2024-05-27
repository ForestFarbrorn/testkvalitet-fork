class QuestionDB:
    def __init__(self) -> None:
        self.db = []

    def add_question(self, question):
        qid = len(self.db)
        question.qid = qid
        self.db.append(question)

        return question

    def get_question(self, qid):
        return self.db[qid]