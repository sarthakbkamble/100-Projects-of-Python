import pandas 

# Converting the CSV file data to a Dataframe
# Read the CSV containing letters and their corresponding NATO phonetic code words
nato_phonetic_alphabet_data = pandas.read_csv("C:/new/100-Projects-of-Python/Day-26-NATO-alphabet-project/nato_phonetic_alphabet.csv")

#Converting dataframe to dictionary
# Use dictionary comprehension to map each letter to its phonetic code from the DataFrame rows
nato_phonetic_alphabet_dict = {row.letter :row.code for (index,row) in nato_phonetic_alphabet_data.iterrows()}

#Getting input
# Prompt the user for a word and standardize it to uppercase to match the dictionary keys
word = input("Enter a word:").upper()

#Converting word to list
# Explode the input string into a list of individual character strings
word_list = [letter for letter in word]

# Loop to get the Nato words
# Map each character in the word to its phonetic code counterpart using a list comprehension
nato_word_list = [nato_phonetic_alphabet_dict[letter] for letter in word_list]

#printing the nato word list
# Output the final list of phonetic words to the console
print(nato_word_list)