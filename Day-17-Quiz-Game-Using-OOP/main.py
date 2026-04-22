from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

# Initialize an empty list to store the collection of Question objects
question_bank =[]

# Loop through the raw question data to instantiate Question objects and populate the question bank
for quest_list in question_data:
    text_from_list = quest_list["text"]
    answer_from_list = quest_list["answer"]
    question_bank.append(Question(text_from_list,answer_from_list))


# Initialize the quiz management engine with the prepared question bank
quiz = QuizBrain(question_bank)

# Display the game logo and run the game loop until all questions have been answered
print(logo)
while quiz.still_has_questions():
    quiz.next_question()

# Display the final completion message and the user's total score statistics
print("You have completed the quiz.")
print(f"Your final score is : {quiz.score}/{quiz.question_number}")