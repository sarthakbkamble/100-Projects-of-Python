import art, game_data, random

def compare(name1, name2):
    """
    Compares the 'follower_count' of two dictionary objects.
    Returns 'A' if the first object has more followers, or 'B' if the second has more.
    Used to validate the user's input against the actual data.
    """
    followers_of_1 = name1["follower_count"]
    followers_of_2 = name2["follower_count"]
    if followers_of_1 > followers_of_2:
        return "A"
    elif followers_of_1 < followers_of_2:
        return "B"

def get_name_data():
    """
    Accesses the 'data' list from game_data and returns one random 
    dictionary containing name, follower count, description, and country.
    """
    return random.choice(game_data.data)

# --- Initial Game Setup ---
# Initialize the first two opponents and the starting score.
name_A = get_name_data()
name_B = get_name_data()
user_score = 0
continue_game = True

def play_game(name_A, name_B):
    """
    A helper function to refresh the UI. 
    Displays the game logo, current score, and the formatted data for both opponents.
    """
    print(art.logo)
    print(f" You're right! Current score: {user_score}.")
    print(f"Compare A: {name_A['name']}, a {name_A['description']}, from {name_A['country']}")
    print(art.vs)
    print(f"Against B: {name_B['name']}, a {name_B['description']}, from {name_B['country']}")

# --- Main Game Loop ---
while continue_game:
    correct_guess = True
    # Initial display for the very first round
    print(art.logo)
    print(f"Compare A: {name_A['name']}, a {name_A['description']}, from {name_A['country']}")
    print(art.vs)
    print(f"Against B: {name_B['name']}, a {name_B['description']}, from {name_B['country']}")

    while correct_guess:
        user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        # Logic Check: Compare user input to the result of the compare() function
        if user_answer == compare(name_A, name_B):
            print("\n" * 20) # Clear screen for the next round
            user_score += 1
            
            # Rotation Logic: Previous 'B' becomes the new 'A', and a new 'B' is generated
            next_random_name = get_name_data()
            play_game(name_B, next_random_name)
            name_A = name_B
            name_B = next_random_name
        else:
            # Game Over State
            print("\n" * 20)
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {user_score}")
            correct_guess = False
            
    # Exit condition for the outer loop
    continue_game = False