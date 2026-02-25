🛠 Project 17.2: Turtle Race
Focus: Object Instances & Concurrent State Logic.

🐢 Multi-Instance Simulation Engine
A competitive simulation demonstrating the instantiation of multiple independent objects and the management of concurrent movement states.

Object Instantiation: Utilizes a factory-style for loop to generate six distinct Turtle instances, each possessing independent color attributes and coordinate properties.

Coordinate Mapping: Implemented a strategic positioning system using a list of Y-coordinates to align instances along the vertical axis, ensuring a standardized starting grid at the x=−230 vector.

Concurrent Execution Loop: Engineered a while loop that iterates through the all_turtles list, applying randomized distance increments to each instance to simulate a real-time race environment.

Collision Detection (Boundary Check): Features a finish-line trigger based on x-coordinate evaluation (turtle.xcor() > 230), which serves as the primary exit condition for the simulation state.

User Input Validation: Integrates a graphical textinput layer to capture user predictions, comparing the final winning object's pencolor() attribute against the stored user string to determine the game outcome.