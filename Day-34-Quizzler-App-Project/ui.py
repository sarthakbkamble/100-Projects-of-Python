THEME_COLOR = "#375362"
GREEN_COLOR = "#499A13"
RED_COLOR = "#CE2626"

from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface :
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.canvas = Canvas(width=300,height=250)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        true_image = PhotoImage(file=r"C:\sarthak\100-Projects-of-Python\Day-34-Quizzler-App-Project\images\true.png")
        false_image = PhotoImage(file=r"C:\sarthak\100-Projects-of-Python\Day-34-Quizzler-App-Project\images\false.png")

        self.true_button = Button(image=true_image,command=self.true_button_pressed)
        self.true_button.config(padx=20,pady=20,highlightthickness=0)
        self.true_button.grid(column=0,row=2)

        self.false_button = Button(image=false_image,command=self.false_button_pressed)
        self.false_button.config(padx=20,pady=20,highlightthickness=0)
        self.false_button.grid(column=1,row=2)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question text",
            fill=THEME_COLOR,
            font=("Arial",15,"italic"))

        self.score = Label(text="Score : 0",fg="white",bg=THEME_COLOR,font=("Arial",20,"normal"))
        self.score.grid(column=1,row=0)
        
        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text= q_text)

        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the Quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def false_button_pressed(self):
        self.give_feedback(is_right= self.quiz.check_answer(user_answer="False"))
    def true_button_pressed(self):
        self.give_feedback(is_right= self.quiz.check_answer(user_answer="True"))
        
    def give_feedback(self,is_right):
        if is_right==True:
            self.canvas.config(bg=GREEN_COLOR)
        else:
            self.canvas.config(bg=RED_COLOR)
        self.window.after(1000,self.get_next_question)
        
