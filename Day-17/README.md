🛠 Project 15: Quiz Game
Focus: Class Construction & Attribute Methods.

🧠 Trivia Intelligence Engine
A modular quiz system utilizing Object-Oriented Programming to manage dynamic data sets and maintain game state through class-based logic.

Model-Logic Separation: Engineered a dedicated Question class to serve as a data model, ensuring each quiz item is an independent object with strictly defined text and answer attributes.

Dynamic Data Ingestion: Implemented a constructor loop that parses raw dictionary data from an external module (data.py) and transforms it into a centralized question_bank of objects.

Brain-Class Architecture: Developed a QuizBrain class to handle the core mechanics of the game. This centralizes the logic for tracking the current question number, user score, and input validation in one manageable object.

Stateful Iteration: Utilizes a custom .still_has_questions() method to drive the main execution loop, demonstrating how class methods can control program flow based on internal object attributes.

Modular Dependency Injection: Successfully integrates multiple local modules (question_model, quiz_brain, data, art), showcasing a professional approach to organizing a multi-file Python project for better maintainability.