🛠 Project 12: Higher Lower Game
Data Extraction & Object Rotation Logic.

📈 Social Popularity Engine
An interactive comparison game that challenges users to evaluate social media metrics through dynamic data fetching and iterative state management.

Dictionary-Driven Data Access: Leverages a complex dataset of nested dictionaries. The engine programmatically extracts specific key-value pairs (name, follower_count, description) to build dynamic string templates for the UI.

Object Rotation Logic: Implemented a "sliding window" algorithm where the previous round's winner (Opponent B) is reassigned as the next round's base (Opponent A). This demonstrates efficient variable reassignment and memory management.

Bi-Directional Evaluation: Engineered a compare() function that acts as a truth-source, returning standardized character flags ('A' or 'B') to validate user input against raw numerical data.

Recursive-Style UI Refresh: Utilizes a helper function, play_game(), to handle terminal rendering. This encapsulates the print logic, allowing the main loop to focus exclusively on score increments and logic checks.

Persistent State Management: Tracks the session through a nested while loop structure, allowing the game to sustain an infinite runtime as long as the user maintains a correct_guess streak.