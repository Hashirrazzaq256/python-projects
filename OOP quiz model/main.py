# This program let user play a Quiz of True and False
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)# creating an object of quizbrain class
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"your score was {quiz.score}/{quiz.question_number}")
