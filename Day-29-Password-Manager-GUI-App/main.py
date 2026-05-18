from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    # Clear any password currently sitting in the entry box before inserting a new one
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []

    # Use list comprehensions to generate a randomized set of letters, symbols, and numbers
    letters_list = [choice(letters) for item in range(randint(8, 10))]
    symbols_list = [choice(symbols) for item in range(randint(2, 4))]
    numbers_list = [choice(numbers) for item in range(randint(2, 4))]
    
    # Combine the three character sets and shuffle them to randomize the order
    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    # Join the character list into a single password string
    password = "".join(password_list)

    # Insert the generated password into the GUI entry box and copy it to the system clipboard
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Retrieve current values written in the UI entry textboxes
    password = password_entry.get()
    username = username_entry.get()
    website = website_entry.get()

    
    # Alert the user with a popup box if they forgot to fill out key fields
    if len(website) ==0  or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        # Prompt user with a confirmation popup displaying the entered credentials
        is_ok = messagebox.askokcancel(title=website, message=f"These are details entered: \nEmail:{username}"
                                   f"\nPassword: {password} \nIs it okay to save?")
        if is_ok:
            # Append the structured credentials to our persistent local data text file
            with open("C:/new/100-Projects-of-Python/Day-29-Password-Manager-GUI-App/data.txt","a") as file:
                file.write(f"{website} | {username} | {password}\n")

            # Reset the input fields to prepare for the next credential entry
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website.focus()
    
    
# ---------------------------- UI SETUP ------------------------------- #
# window setup with title and generous padding
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

# canvas setup to show the logo image
canvas = Canvas(height=200,width=200)
lock_image = PhotoImage(file="C:/new/100-Projects-of-Python/Day-29-Password-Manager-GUI-App/logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1,row=0)

# labels for input indicators
website_label = Label(text="Website:",font=("arial",10,"normal"))
website_label.grid(column=0,row=1)

username_label = Label(text="Email/Username:",font=("arial",10,"normal"))
username_label.grid(column=0,row=2)

password_label = Label(text="Password:",font=("arial",10,"normal"))
password_label.grid(column=0,row=3)

# buttons configured for actions
add_button = Button(text="Add",font=("arial",10,"normal"),width=26, command=save)
add_button.grid(column=1,row=4,columnspan=2,sticky="ew")


generate_button = Button(text="Generate Password",font=("arial",10,"normal"),command=generate_password)
generate_button.grid(column=2,row=3)


# text entries configured with span and focus priorities
website_entry = Entry(width=35,font=("arial",10,"normal"))
website_entry.grid(column=1,row=1,columnspan=2,sticky="ew")
website_entry.focus()

username_entry = Entry(width=35,font=("arial",10,"normal"))
username_entry.insert(0,"abcd@gmail.com")
username_entry.grid(column=1,row=2,columnspan=2,sticky="ew")

password_entry = Entry(width=21,font=("arial",10,"normal"))
password_entry.grid(column=1,row=3,sticky="ew")


# Run application main loop
window.mainloop()