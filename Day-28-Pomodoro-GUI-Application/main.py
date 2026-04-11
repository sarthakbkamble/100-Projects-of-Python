from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="Timer",fg=GREEN)
    check_marks.config(text="")
    global reps 
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    #If it's the 8th rep:
    if reps% 8==0:
        count_down(long_break_sec)
        timer.config(text="Long Break",font=(FONT_NAME,35,"bold"),fg=RED,bg=YELLOW)
    #if it's 2nd/4th/6th rep:
    elif reps%2==0:
        count_down(short_break_sec)
        timer.config(text="Short Break",font=(FONT_NAME,35,"bold"),fg=PINK,bg=YELLOW)
    #If it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        timer.config(text="Work",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_min<10:
        count_min=f"0{count_min}"

    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global my_timer
        my_timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks =""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks+="✓"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file="C:/new/100-Projects-of-Python/Day-28-Pomodoro-GUI-Application/tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

#Timer text

timer = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
timer.grid(row=0,column=1)


#check mark 
check_marks = Label(font=(FONT_NAME,15,"bold"),fg=GREEN,bg=YELLOW)
check_marks.grid(row=3,column=1)



#start button
button_1 = Button(text="Start",font=(FONT_NAME,10,"bold"),command=start_timer)
button_1.grid(row=2,column=0)

#reset button
button_2 = Button(text="Reset",font=(FONT_NAME,10,"bold"),command=reset_timer)
button_2.grid(row=2,column=2)

window.mainloop()