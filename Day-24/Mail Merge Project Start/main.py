#TODO: Create a letter using starting_letter.txt 
with open("/new/100-Projects-of-Python/Day-24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as starting_letter:
    blueprint_of_letter = starting_letter.readlines(1)
    print(blueprint_of_letter)
    
    
#for each name in invited_names.txt


#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp