🛠 Project 6: Hangman Game
Focus: State Management & Game Loops.

😵 Hangman Engine
A state-based CLI game demonstrating complex while loops, list manipulation,
and external dependency management.

State Management: Tracks game status through a game_over boolean and
a lives counter to manage the iterative game loop.

Dynamic UI Rendering: Implemented a placeholder system using list
iteration to provide real-time visual feedback on user progress.

Dependency Injection: Imports word lists and ASCII art from
external local modules (hangman_words, hangman_art) to keep the main.py controller
clean and focused.