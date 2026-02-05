import random
import symbols
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,1)
value = user_choice-computer_choice
list_of_symbols = [symbols.rock, symbols.paper,symbols.scissors]

#printing user and computer choice
print(list_of_symbols[user_choice])

print("Computer choose:")
print(list_of_symbols[computer_choice])
#conditions
if value==0:
    print("Its a draw.")
elif value == 1:
    print("You Win !!")
else :
    print("You Lose, boo!!")