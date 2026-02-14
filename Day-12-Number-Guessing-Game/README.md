🛠 Project 11: Number Guessing Game
Scope Management & Global vs. Local State.

🎯 Precision Guessing Engine
A logic-driven game demonstrating the application of variable scope, comparative algorithms, and interactive control loops.

Dynamic Difficulty Scaling: Implemented a multi-tiered difficulty system that programmatically adjusts the lives constant based on user input, demonstrating flexible state initialization.

Comparative Logic abstraction: Engineered a dedicated checking_guess() function to handle numerical evaluation. This modular approach separates the comparison logic from the main execution loop for better readability.

Scope & State Manipulation: Manages a global game state using boolean flags (game_over, play) while utilizing functional returns to update the remaining attempts counter across different scopes.

Input Sanitization: Features a case-insensitive validation layer (.lower()) and error handling for invalid difficulty selections to ensure a crash-resistant user experience.

Iterative Feedback Loop: Developed a "trapped" while loop that provides real-time proximity feedback ("Too high" vs "Too low"), guiding the user toward the solution through successive approximation.