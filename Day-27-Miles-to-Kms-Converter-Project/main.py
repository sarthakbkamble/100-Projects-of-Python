#importing everything from tkinter
from tkinter import *

# window
# Initialize the main window, set the title, set minimum dimensions, and add padding
window = Tk()
window.title("Mile to KM converter")
window.minsize(width=450,height=250)
window.config(padx=40,pady=50)


#labels
# Create and position text labels across the grid to structure the interface
label_1 = Label(text="Miles",font=("arial",18,"normal"))
label_1.grid(column=2,row=0)

label_2 = Label(text="is equal to",font=("arial",18,"normal"))
label_2.grid(column=0,row=1)

label_3 = Label(text="Km",font=("arial",18,"normal"))
label_3.grid(column=2,row=1)

# This dynamic label will display the final calculated result
label_4 = Label(font=("arial",18,"normal"))
label_4.grid(column=1,row=1)

#input
# Set up a text input field for the user to type their mileage values, defaulting to "0"
entry = Entry(width=10,font=(20))
entry.insert(END,string="0")
entry.grid(column=1,row=0)


# function to convert miles to kms
def convert():
    # Fetch the input string, cast it to a float, and apply the metric conversion multiplier
    miles = float(entry.get())
    kms = round(miles*1.609344,2)
    # Update the dynamic results label with the newly calculated kilometer value
    label_4.config(text=kms,font=("arial",18,"normal"))
    


#button
# Create a button that triggers the conversion calculation function when clicked
button = Button(text="Calculate",font=("arial",18,"normal"), command=convert)
button
button.grid(column=1,row=2)

#keeps the window open
# Run the application's event-monitoring loop to keep the GUI alive and interactive
window.mainloop()