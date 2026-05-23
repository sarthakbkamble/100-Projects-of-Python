from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# --- DATA INITIALIZATION ---
# Try to load progress from 'words_to_learn.csv', otherwise load the original complete list
try:
    data = pandas.read_csv(r"C:\sarthak\100-Projects-of-Python\Day-31-Flash-Card-App\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"C:\sarthak\100-Projects-of-Python\Day-31-Flash-Card-App\data\french_words.csv")
    # Convert DataFrame to a list of row dictionaries e.g. [{"French": "word", "English": "word"}]
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# --- CARD NAVIGATION & FLIPPING ---

def next_card():
    """Selects a random word from the vocabulary list and displays its French front side."""
    global current_card, flip_timer
    # Cancel the previous active timer to prevent premature card flipping
    window.after_cancel(flip_timer)
    
    # Pick a random dictionary entry from our learning list
    current_card = random.choice(to_learn)
    
    # Render the front of the card with black-colored text
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    
    # Start a fresh 3-second timer to automatically show the English translation
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flips the current card over to show the English translation on a dark background."""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# --- SAVING PROGRESS ---

def is_known():
    """Removes the current card from the learning pool and updates the persistent save file."""
    to_learn.remove(current_card)
    
    # Convert the remaining dictionary items back to a DataFrame and write to a CSV
    data = pandas.DataFrame(to_learn)
    data.to_csv(r"C:\sarthak\100-Projects-of-Python\Day-31-Flash-Card-App\data\words_to_learn.csv", index=False)
    
    # Load the next word
    next_card()


# --- UI SETUP ---

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Establish a baseline timer placeholder that gets managed dynamically by functions
flip_timer = window.after(3000, func=flip_card)

# Set up the flashcard drawing Canvas widget
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=r"C:\sarthak\100-Projects-of-Python\Day-31-Flash-Card-App\images\card_front.png")
card_back_img = PhotoImage(file=r"C:\sarthak\100-Projects-of-Python\Day-31-Flash-Card-App\images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Interactive control buttons
cross_image = PhotoImage(file=r"C:\sarthak\100-Projects-of-Python\Day-31-Flash-Card-App\images\wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=r"C:\sarthak\100-Projects-of-Python\Day-31-Flash-Card-App\images\right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Display the first card automatically upon loading
next_card()

window.mainloop()