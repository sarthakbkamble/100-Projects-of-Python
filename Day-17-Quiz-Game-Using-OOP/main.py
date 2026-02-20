from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo
question_bank =[]

for quest_list in question_data:
    text_from_list = quest_list["text"]
    answer_from_list = quest_list["answer"]
    question_bank.append(Question(text_from_list,answer_from_list))


quiz = QuizBrain(question_bank)

print(logo)
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz.")
print(f"Your final score is : {quiz.score}/{quiz.question_number}")