import pandas 

# Converting the CSV file data to a Dataframe
nato_phonetic_alphabet_data = pandas.read_csv("C:/new/100-Projects-of-Python/Day-26-NATO-alphabet-project/nato_phonetic_alphabet.csv")
#Converting dataframe to dictionary
nato_phonetic_alphabet_dict = {row.letter :row.code for (index,row) in nato_phonetic_alphabet_data.iterrows()}

#Getting input
word = input("Enter a word:").upper()

#Converting word to list
word_list = [letter for letter in word]

# Loop to get the Nato words
nato_word_list = [nato_phonetic_alphabet_dict[letter] for letter in word_list]

#printing the nato word list
print(nato_word_list)