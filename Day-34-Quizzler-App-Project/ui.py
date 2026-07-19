THEME_COLOR = "#375362"
# Custom feedback colors defined to visually represent right/wrong answers
GREEN_COLOR = "#499A13"
RED_COLOR = "#CE2626"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Establish a reference connection to the quiz logic coordinator
        self.quiz = quiz_brain

        # Set up the primary GUI display window container with customized padding
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create a central drawing Canvas widget to hold the question text
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Load button representation images from system path
        true_image = PhotoImage(file=r"C:\sarthak\100-Projects-of-Python\Day-34-Quizzler-App-Project\images\true.png")
        false_image = PhotoImage(file=r"C:\sarthak\100-Projects-of-Python\Day-34-Quizzler-App-Project\images\false.png")

        # Configure and align the green "True" button
        self.true_button = Button(image=true_image, command=self.true_button_pressed)
        self.true_button.config(padx=20, pady=20, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        # Configure and align the red "False" button
        self.false_button = Button(image=false_image, command=self.false_button_pressed)
        self.false_button.config(padx=20, pady=20, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        # Draw the dynamic text object inside the Canvas with custom boundaries for wrapping long text
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280, # Limits text width so words wrap cleanly to new lines instead of overflowing
            text="Some Question text",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic")
        )

        # Score display indicator label placed at the top-right
        self.score = Label(text="Score : 0", fg="white", bg=THEME_COLOR, font=("Arial", 20, "normal"))
        self.score.grid(column=1, row=0)
        
        # Load and display the first question automatically upon startup
        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        """Resets the canvas background and populates it with the next quiz question."""
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            # Update the score label and load the next question text
            self.score.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            # Handle the end-of-game scenario by disabling both inputs and notifying the player
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the Quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def false_button_pressed(self):
        """Callback function triggered when the user clicks the False button."""
        self.give_feedback(is_right=self.quiz.check_answer(user_answer="False"))

    def true_button_pressed(self):
        """Callback function triggered when the user clicks the True button."""
        self.give_feedback(is_right=self.quiz.check_answer(user_answer="True"))
        
    def give_feedback(self, is_right):
        """
        Temporarily updates the canvas color depending on the answer validation accuracy,
        then schedules the interface to load the next question after 1000ms.
        """
        if is_right == True:
            self.canvas.config(bg=GREEN_COLOR)
        else:
            self.canvas.config(bg=RED_COLOR)
        # Schedule next action: Pause for 1 second to let the user see the result before loading the next question
        self.window.after(1000, self.get_next_question)