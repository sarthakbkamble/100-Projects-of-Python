Project 7 : Caesar Cipher Engine

A cryptographic utility demonstrating bi-directional data transformation
through shift-based logic and modular mathematics.

Mathematical Integrity: Employs modulo arithmetic (shifted_position %= len(alphabet))
to handle alphabet "wrap-around," ensuring shifts beyond 'z' return to 'a' without index errors.

Cryptographic Logic: Uses a unified function for both encryption and decryption
by programmatically converting the shift_amount to a negative integer for "decode" requests.

Non-Alpha Preservation: Features a conditional filter that identifies characters
outside the alphabet (spaces, numbers, symbols) and appends them to the output unchanged.

Input Validation Architecture: Implements a nested while loop to
trap and sanitize user inputs for the direction and restart variables, ensuring the
program only proceeds with valid commands.

State Management: Tracks global execution status through a run_cipher_program boolean,
allowing for an iterative user experience that only terminates upon explicit command.