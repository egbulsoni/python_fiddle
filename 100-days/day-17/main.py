from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))


# for li in question_bank:
#     print(li.text)
#     print(li.answer)

qb = QuizBrain(question_bank)
qb.next_question()