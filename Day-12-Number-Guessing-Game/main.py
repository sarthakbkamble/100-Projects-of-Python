# Imported libraries
import art, random

def checking_guess(selected_number,guessed_num):
    """
    Takes two inputs random selected number and guessed number by user.
    compares whether the guessed number is high or low.
    Return : edits the life
    """
    if guessed_num<selected_number:
        print("Too low.")
        print("Guess again.")
        return lives-1
    elif guessed_num>selected_number:
        print("Too high.")
        print("Guess again.")
        return lives-1

    return None


game_over = False
play = True
lives=0

# Loop to continue the game
while play:
    # Printing the logo
    print(art.logo)

    # Generating random number
    num = random.choice(range(1, 101))

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Asking the user for the game difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

    # Conditions for the specific selected difficulty
    if difficulty == "hard":
       lives=5
       print(f"You have {lives} attempts remaining to guess the number.")

       # Checks the guess, edits life and runs until the user lose or win the game.
       while not game_over:
           guess=int(input("Make a guess:"))
           if num == guess:
               print(f"You got it! The answer was {num}.")
               game_over=True
           else:
               if lives == 1:
                   print("You've run out of guesses. Refresh the page to run again.")
                   game_over = True
               else:
                   lives = checking_guess(selected_number=num, guessed_num=guess)
                   print(f"You have {lives} attempts remaining to guess the number.")
                   print("\n")

    # Conditions for the specific selected difficulty
    elif difficulty == "easy":
        lives=10
        print(f"You have {lives} attempts remaining to guess the number.")

        # Checks the guess, edits life and runs until the user lose or win the game.
        while not game_over:
            guess = int(input("Make a guess:"))

            if num == guess:
                print(f"You got it! The answer was {num}.")
                game_over=True
            else:
                if lives == 1:
                    print("You've run out of guesses. Refresh the page to run again.")
                    game_over = True
                else:
                    lives = checking_guess(selected_number=num, guessed_num=guess)
                    print(f"You have {lives} attempts remaining to guess the number.")
                    print("\n")
    else:
        print("Invalid Input.")
    # Game Ends
    play = False