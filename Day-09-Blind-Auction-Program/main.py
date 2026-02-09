#Project 08 Blind Auction Pogram
import art
# Display the program logo from the 'art' module
print(art.logo)

# Initialize an empty dictionary to store names as keys and bid amounts as values
bidding_Data = {}
# Control variable to keep the auction loop running
auction_is_active = True

while auction_is_active:
    # Gather user data for the current bidder
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    # Save the input into the dictionary
    bidding_Data[name] = bid

    # Input validation loop to check if the auction should continue
    ask_for_new_bidder = True
    while ask_for_new_bidder:
        new_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

        if new_bidders == "yes":
            auction_is_active = True
            ask_for_new_bidder = False
            # Clear the screen (print 100 new lines) to keep bids secret from next user
            print("\n" * 100)
        elif new_bidders == "no":
            # Exit both the validation loop and the main auction loop
            auction_is_active = False
            ask_for_new_bidder = False
        else:
            # Handle unexpected text input
            print("Invalid input!")
            ask_for_new_bidder = True

# Initialize variables to track the winning bidder and their amount
highest_bid = 0
highest_bidder_name = ""

# Iterate through the dictionary keys to find the largest value
for key in bidding_Data:
    # If the current bid in the loop is larger than the recorded highest_bid
    if highest_bid <= bidding_Data[key]:
        highest_bid = bidding_Data[key]
        highest_bidder_name = key

# Final output displaying the winner of the auction
print(f"The winner is {highest_bidder_name} with a bid of ${highest_bid}.")