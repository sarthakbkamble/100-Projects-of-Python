# Opening format of the letter 
with open("C:/new/100-Projects-of-Python/Day-24/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r")   as file:
    starting_letter = file.read()

# Getting the names of the people
with open("C:/new/100-Projects-of-Python/Day-24/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    list_of_name = file.readlines()

# loop for writing a letter to each individual name and saving them into their name file
for name in list_of_name:
    name = name.strip()
    letter = starting_letter.replace("[name]",name)
    with open(f"C:/new/100-Projects-of-Python/Day-24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}",mode="w") as file:
        file.write(letter)


    






