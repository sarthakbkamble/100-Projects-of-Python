# Opening the format of the letter 
# Read the base template file containing the generic message draft and placeholder key
with open("C:/new/100-Projects-of-Python/Day-24/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r")   as file:
    starting_letter = file.read()

# Getting the names of the people
# Read the source text file containing all the individual invitee names line-by-line
with open("C:/new/100-Projects-of-Python/Day-24/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    list_of_name = file.readlines()

# loop for writing a letter to each individual name and saving them into their name file
# Clean each parsed name, swap the placeholder text, and write a unique letter for each guest
for name in list_of_name:
    # Remove leading/trailing whitespaces and newline characters (\n) from each parsed string
    name = name.strip()
    # Substitute the target placeholder template marker with the current guest's name
    letter = starting_letter.replace("[name]",name)
    # Write the customized letter string into a newly generated text file named after the recipient
    with open(f"C:/new/100-Projects-of-Python/Day-24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}",mode="w") as file:
        file.write(letter)