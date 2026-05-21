from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip, json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    # Clear any existing password from the input box before inserting a new one
    password_entry.delete(0, END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate lists of random characters with variable lengths
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine lists, shuffle the characters randomly, and join them into a final string
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # Put the generated password into the UI entry field and copy it to the system clipboard
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Gather information entered into the UI text fields
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    # Structure the credential information in a nested dictionary format for JSON storage
    new_data = {
        website:{
            "email":email,
            'password': password,
        }
    }

    # Validate inputs: throw an alert if essential fields are left blank
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            # Try to read and parse the existing JSON data file
            with open(r"C:\sarthak\100-Projects-of-Python\Day-30\3\data.json", "r") as data_file:
                data = json.load(data_file)
                
        except FileNotFoundError:
            # If the data file does not exist yet, write a fresh file using the current entry
            with open(r"C:\sarthak\100-Projects-of-Python\Day-30\3\data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # If reading succeeded, update the parsed dictionary with the new website data
            data.update(new_data)
            # Save the updated dictionary back to the JSON file
            with open(r"C:\sarthak\100-Projects-of-Python\Day-30\3\data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # Clean up the entry boxes and refocus cursor on the website field
            website_entry.delete(0, END)
            password_entry.delete(0, END) 

# ---------------------------- FIND PASSWORD (SEARCH) ----------------------- #
def find_password():
    # Grab the website name to search for
    website = website_entry.get()
    try:
        # Attempt to read the JSON database
        with open(r"C:\sarthak\100-Projects-of-Python\Day-30\3\data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        # Alert the user if they try to search before any database file exists
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        # Check if the requested website key exists in our data dictionary
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            # Present the retrieved credentials in an information popup window
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            # Inform the user if the searched website has no record
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

# Create main container window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create a Canvas widget to present the program's lock logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="C:/sarthak/100-Projects-of-Python/Day-30/3/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0,sticky="e",pady=5)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0,sticky="e",pady=5)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0,sticky="e",pady=5)

# Input Entries
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1, columnspan=2,padx=5,sticky="w")
website_entry.focus() # Auto-focus user cursor on the website input field on startup

email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2,sticky="w",padx=5)
email_entry.insert(0, "angela@gmail.com") # Pre-populate default email address

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1,padx=5,sticky="w")

# Buttons and Grid Alignment Settings
generate_password_button = Button(width=15,text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2,sticky="ew",padx=5)

add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2,pady=10,padx=5,sticky="w")

search_button = Button(text="Search",width=15,command=find_password)
search_button.grid(column=2,row=1,padx=5,sticky="ew")

# Start application event mainloop
window.mainloop()