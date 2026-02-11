import art
import random
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
play_blackjack = True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if play =="y":
    play_blackjack = True
else:
    play_blackjack = False

while play_blackjack:
    print(art.logo)