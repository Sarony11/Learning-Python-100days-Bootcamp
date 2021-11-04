from question_model import Question
from quiz_brain import QuizBrain
from data_geography import question_data

question_bank = []

for question in question_data:
    q = Question(question["text"],question["answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.check_answer(quiz.next_question())
quiz.end_quiz()

    