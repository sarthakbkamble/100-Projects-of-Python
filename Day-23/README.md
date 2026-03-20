🛠 Project 20: Turtle Crossing Capstone
Focus: Game Loop Architecture & Dynamic Difficulty Scaling.

🐢 Traffic Avoidance Engine
A sophisticated "Frogger" style simulation that coordinates autonomous entity generation, player input, and progressive difficulty curves through synchronized class interactions.

Autonomous Entity Management: Implements a CarManager class that serves as a factory for obstacle generation. It handles the instantiation, randomized Y-axis placement, and horizontal translation of multiple "car" objects within a centralized collection.

Dynamic Difficulty Scaling: Features an adaptive speed controller. Upon a successful crossing, the engine triggers an increase_speed() method, programmatically shortening the frame-update latency or increasing the pixel-per-frame constant.

Coordinate-Based Collision Physics: Utilizes a high-frequency polling loop to evaluate the distance() between the player and every active car instance. A collision is triggered if the scalar distance drops below a 20-pixel threshold, demonstrating efficient list-traversal logic.

State Reset & Level Advancement: Coordinates a multi-step transition when the player reaches the "finish line" boundary. This involves resetting the player's Cartesian coordinates, incrementing the scoreboard level, and flushing/accelerating the traffic state.

Refined Game Loop Timing: Uses time.sleep(0.1) in conjunction with screen.tracer(0) to regulate the frame rate, ensuring that the manual screen.update() calls result in smooth, non-stuttering animations.

Event-Driven Navigation: Maps the "Up" keyboard interrupt to a specific move() method, restricting player movement to a single axis to maintain the core mechanical challenge of the simulation.