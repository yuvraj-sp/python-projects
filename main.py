from Question_class import Question
from data import question_data
from Quiz_Brain import QuizBrain


question_bank=[]
for i in question_data:
    question_quiz=i["text"]
    question_answer=i["answer"]
    new_question=Question(question_quiz,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("you have completed the quiz.")
print(f"Your final score was : {quiz.score}/{quiz.question_number}")