THEME_COLOR = "#375362"

from tkinter import *

class QuizInterface :
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.canvas = Canvas(width=300,height=250)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        true_image = PhotoImage(file=r"C:\sarthak\100-Projects-of-Python\Day-34-Quizzler-App-Project\images\true.png")
        false_image = PhotoImage(file=r"C:\sarthak\100-Projects-of-Python\Day-34-Quizzler-App-Project\images\false.png")

        self.true_button = Button(image=true_image)
        self.true_button.config(padx=20,pady=20,highlightthickness=0)
        self.true_button.grid(column=0,row=2)

        self.false_button = Button(image=false_image)
        self.false_button.config(padx=20,pady=20,highlightthickness=0)
        self.false_button.grid(column=1,row=2)

        self.canvas.create_text(150,125,text="Some Question text",fill=THEME_COLOR,font=("Arial",15,"italic"))

        self.score = Label(text="Score : 0",fg="white",bg=THEME_COLOR,font=("Arial",20,"normal"))
        self.score.grid(column=1,row=0)
        

        self.window.mainloop()