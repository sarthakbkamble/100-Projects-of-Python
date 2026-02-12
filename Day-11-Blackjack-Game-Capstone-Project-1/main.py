import random
from art import logo

def deal_card():
    """
    Selects a random card from a standard deck where J, Q, K are 10 
    and Ace is 11. Returns the integer value of the card.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    Takes a list of card values and calculates the total score.
    Checks for a Blackjack (Ace + 10) and returns 0 to represent it.
    Also handles the 'Ace conversion' (11 becomes 1) if the score exceeds 21.
    """
    # Check for Blackjack (2 cards totaling 21)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Logic for Ace: If total > 21 and there is an 11, swap 11 for 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    """
    Receives user and computer scores and evaluates the winning condition
    based on Blackjack rules. Returns a string message with the result.
    """
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    """
    Main game engine. Manages the game state, handles user turns (hitting/passing),
    automates the computer's turn, and triggers the final comparison.
    """
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial 2 cards to both players
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's Turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # End turn if someone has Blackjack or User busts
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's Turn: Dealer must hit until score is at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Global Loop: Allows the user to restart the game repeatedly
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20) # Clears the console for a fresh game
    play_game()