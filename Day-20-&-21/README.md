🛠 Project 18 : Snake Game Engine
Class Inheritance & Collision Physics.

🐍 Classic Snake Simulation
A multi-module application demonstrating advanced Object-Oriented Programming, focusing on coordinate-based collision detection and dynamic object growth.

Class Inheritance: Extends the Turtle class within the Food and Scoreboard modules, allowing these components to inherit graphical properties while implementing custom behaviors like .refresh() and .increase_score().

Screen Buffer Management: Utilizes screen.tracer(0) and screen.update() to disable automatic screen updates. This manual refresh cycle eliminates flickering and enables smooth, synchronized movement of multi-segment entities.

Proximity Detection Logic: Implemented mathematical collision checks using the .distance() method. The engine triggers state changes (food consumption or tail collision) when the scalar distance between two objects falls below a specific pixel threshold.

Dynamic Slicing & Iteration: Employs Python's list slicing (snake.segments[1:]) to iterate through the snake's body while excluding the head, optimizing tail-collision checks and preventing self-intersection errors.

Boundary Constraint Logic: Features a centralized game-loop monitor that evaluates the head's x/y coordinates against the screen's edge, triggering a game_over sequence upon a boundary breach.

Modular Orchestration: Coordinates four distinct local modules (snake, food, scoreboard, main) to maintain a clean separation of concerns, where each class handles its own state and rendering.