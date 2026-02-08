# Project 7 Caesar Cipher
import art

# Display the logo from the art module at the start
print(art.logo)

# Reference list of characters for the cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Core function to handle both encryption and decryption
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    # For decoding, we reverse the shift direction by making the amount negative
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        # Check if the character is a letter; if not (space/number), keep it as is
        if letter in alphabet:
            # Find the index, apply the shift, and use modulo to wrap around 'z' to 'a'
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Control variable to keep the program running
run_cipher_program = True

while run_cipher_program:
    # Input validation loop for 'encode' vs 'decode'
    correct_input = True
    while correct_input:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == "encode" or direction == "decode":
            correct_input = False
        else:
            print("Invalid input!!")
            
    # Gather user message and the shift key
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Execute the cipher function
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user if they want to run the program again
    ask_to_restart = True
    while ask_to_restart:
        choice = (input("Do you want to restart the Cipher Program? Y or N:")).upper()
        if choice == "Y":
            run_cipher_program = True
            ask_to_restart = False
        elif choice == "N":
            run_cipher_program = False
            ask_to_restart = False
            print("Thank you for using caesar cipher.")
        else:
            print("Invalid Input! Answer Y or N only.")