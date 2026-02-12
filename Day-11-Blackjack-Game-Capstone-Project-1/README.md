🛠 Project 10: Blackjack Capstone
Heuristic Logic & Dynamic State Evaluation.

🃏 Professional Blackjack Engine
A complex game-state simulator implementing the official "Las Vegas" ruleset through modular function architecture and conditional probability.

Dynamic Scoring Algorithm: Features a sophisticated calculate_score function that evaluates game-ending conditions (Blackjack) and implements "soft hand" logic—automatically revaluing Aces from 11 to 1 to prevent a bust.

Heuristic AI Automation: Implements an automated dealer intelligence that follows standard casino protocols, programmatically hitting until a minimum threshold of 17 is reached.

Game Lifecycle Management: Uses a flag-based is_game_over state controller to manage transitions between the user's iterative turn and the computer's automated execution.

Modular Comparison Logic: Decouples win/loss evaluation into a dedicated compare() utility, utilizing a cascading if/elif structure to prioritize high-level game states like natural Blackjacks over simple numeric totals.

Recursive Session Control: Engineered a global loop that facilitates continuous gameplay sessions, including console-clearing logic to reset the visual environment for each iteration.