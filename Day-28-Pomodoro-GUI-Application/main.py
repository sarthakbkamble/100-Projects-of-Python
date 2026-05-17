from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
# Color palette and font styles for the Pomodoro interface
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# Time configuration constants (in minutes)
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # Cancel the active Tkinter window recursive loop timer to stop counting down
    window.after_cancel(my_timer)
    # Reset the visual canvas text, main title label, and checkmark counter
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="Timer",fg=GREEN)
    check_marks.config(text="")
    # Reset the session repetition counter back to zero
    global reps 
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    # Convert configuration minutes into seconds
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    # If it's the 8th rep: Trigger a long break
    if reps% 8==0:
        count_down(long_break_sec)
        timer.config(text="Long Break",font=(FONT_NAME,35,"bold"),fg=RED,bg=YELLOW)
    # if it's 2nd/4th/6th rep: Trigger a short break
    elif reps%2==0:
        count_down(short_break_sec)
        timer.config(text="Short Break",font=(FONT_NAME,35,"bold"),fg=PINK,bg=YELLOW)
    # If it's the 1st/3rd/5th/7th rep: Trigger a work cycle
    else:
        count_down(work_sec)
        timer.config(text="Work",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # Calculate the remaining minutes and seconds
    count_min = math.floor(count/60)
    count_sec = count%60
    
    # Format single digit minutes with a leading zero
    if count_min<10:
        count_min=f"0{count_min}"

    # Format single digit seconds with a leading zero (e.g., "05" instead of "5")
    if count_sec<10:
        count_sec=f"0{count_sec}"

    # Update the countdown display on the canvas
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    
    # Recursively call this function every 1000ms (1 second) if time remains
    if count>0:
        global my_timer
        my_timer = window.after(1000,count_down,count-1)
    else:
        # Move on to the next work/break session automatically when the countdown hits zero
        start_timer()
        # Append checkmarks on screen for every completed work session (reps/2)
        marks =""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks+="✓"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

# Initialize the main GUI window container with custom padding and a yellow background
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

# Create a canvas widget to lay out the tomato illustration image and the overlay text
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file="C:/new/100-Projects-of-Python/Day-28-Pomodoro-GUI-Application/tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

# Timer Status Header Label
timer = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
timer.grid(row=0,column=1)


# Completed Session Checkmarks Label
check_marks = Label(font=(FONT_NAME,15,"bold"),fg=GREEN,bg=YELLOW)
check_marks.grid(row=3,column=1)


# Action control buttons
button_1 = Button(text="Start",font=(FONT_NAME,10,"bold"),command=start_timer)
button_1.grid(row=2,column=0)

button_2 = Button(text="Reset",font=(FONT_NAME,10,"bold"),command=reset_timer)
button_2.grid(row=2,column=2)

# Run the Tkinter event loop to render the UI and wait for user actions
window.mainloop()