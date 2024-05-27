import sqlite3
from models import Question

class QuestionDB:
    def __init__(self, filename = 'db.sqlite3') -> None:
        self.filename = filename

    def initialize_db(self):
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS questions (qid INTEGER PRIMARY KEY, question TEXT, answer TEXT)')
        conn.commit()
        conn.close()

    def add_question(self, question):
        conn = sqlite3.connect(self.filename)

        c = conn.cursor()
        c.execute('INSERT INTO questions (question, answer) VALUES (?, ?)', (question.question_text, question.answer_text))
        conn.commit()

        question.qid = c.lastrowid

        return question

    def get_question(self, qid):
        conn = sqlite3.connect(self.filename)

        c = conn.cursor()
        c.execute('SELECT * FROM questions WHERE qid = ?', (qid,))

        row = c.fetchone()

        if row is None:
            return None

        return Question(qid=row[0], question_text=row[1], answer_text=row[2])
    
    def get_all_questions(self):
        conn = sqlite3.connect(self.filename)

        c = conn.cursor()
        c.execute('SELECT * FROM questions')

        rows = c.fetchall()

        return [Question(qid=row[0], question_text=row[1], answer_text=row[2]) for row in rows]