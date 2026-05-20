# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

# Load the NATO phonetic alphabet CSV into a Pandas DataFrame
data = pandas.read_csv("C:/sarthak/100-Projects-of-Python/Day-30/2/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
# Map each letter from the DataFrame row directly to its phonetic code representation
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# word = input("Enter a word: ").upper()
# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)


# Flag to manage the verification state of the user's input
correct_input = False

# Loop continuously until the user inputs a valid word containing only alphabetic letters
while not correct_input: 
    word = input("Enter a word: ").upper()
    try:
        # Attempt to map every character in the user's input to the dictionary keys
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        # Triggered if a character (e.g. space, number, symbol) doesn't exist in the alphabet dictionary
        print("Sorry, only letters in the aplhabet please.")
    else:
        # Executes only if the dictionary lookup succeeds for all letters with no exceptions raised
        correct_input=True

# Output the final list of phonetic code words to the console
print(output_list)