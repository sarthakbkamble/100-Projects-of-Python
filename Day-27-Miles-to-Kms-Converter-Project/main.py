#importing everything from tkinter
from tkinter import *

# window
window = Tk()
window.title("Mile to KM converter")
window.minsize(width=450,height=250)
window.config(padx=40,pady=50)


#labels

label_1 = Label(text="Miles",font=("arial",18,"normal"))
label_1.grid(column=2,row=0)

label_2 = Label(text="is equal to",font=("arial",18,"normal"))
label_2.grid(column=0,row=1)

label_3 = Label(text="Km",font=("arial",18,"normal"))
label_3.grid(column=2,row=1)

label_4 = Label(font=("arial",18,"normal"))
label_4.grid(column=1,row=1)

#input
entry = Entry(width=10,font=(20))
entry.insert(END,string="0")
entry.grid(column=1,row=0)


# function to convert miles to kms
def convert():
    miles = float(entry.get())
    kms = round(miles*1.609344,2)
    label_4.config(text=kms,font=("arial",18,"normal"))
    


#button
button = Button(text="Calculate",font=("arial",18,"normal"), command=convert)
button
button.grid(column=1,row=2)

#keeps the window open
window.mainloop()