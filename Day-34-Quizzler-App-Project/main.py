from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import ui

# --- Question Bank Initialization ---
# Create an empty list to store the instantiated Question objects
question_bank = []

# Loop through the raw question dataset fetched from the API
for question in question_data:
    # Extract the question string and correct answer text from each dictionary
    question_text = question["question"]
    question_answer = question["correct_answer"]
    
    # Instantiate a Question object using the extracted details and add it to our bank
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# --- Game Engines Coupling ---
# Initialize the quiz logic engine with the populated question bank list
quiz = QuizBrain(question_bank)

# Initialize the Tkinter Graphical User Interface and link it directly to our quiz logic engine
quiz_ui = ui.QuizInterface(quiz_brain=quiz)

# --- Legacy Console Execution Loop ---
# This terminal loop is commented out because the Tkinter GUI (QuizInterface) 
# now dynamically manages the question progression and game state events.
# while quiz.still_has_questions():
#     quiz.next_question()

# Terminal fallback print statement displayed upon quitting or completion
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")