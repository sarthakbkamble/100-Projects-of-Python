# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("C:/sarthak/100-Projects-of-Python/Day-30/2/nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# word = input("Enter a word: ").upper()
# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)


correct_input = False

while not correct_input: 
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the aplhabet please.")
    else:
        correct_input=True
print(output_list)