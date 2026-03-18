🛠 Project 19: Pong Arcade Game
Focus: Vector Reflection & Multi-Object Interaction.

🏓 Classic Arcade Engine
A high-performance two-player simulation that utilizes coordinate geometry and asynchronous event listening to replicate the physics of a classic arcade game.

Vector Reflection Logic: Engineered a bi-directional "bounce" system. The ball utilizes a bounce_y() method to invert vertical velocity upon wall contact and a bounce_x() method to reflect off paddles, simulating realistic elastic collisions.

Manual Screen Synchronization: Employs my_screen.tracer(0) and my_screen.update() to bypass the default Turtle animation delay. This allows the game loop to handle object positioning at a much higher frequency, ensuring jitter-free movement during high-speed play.

Complex Collision Detection: Implemented a dual-condition trigger for paddle contact. The system evaluates both the scalar distance() from the paddle center and the exact xcor() threshold to differentiate between a successful block and a missed point.

Dynamic Game Balancing: Features a variable moving_speed attribute within the Ball object. This allows the program to programmatically increase difficulty by reducing time.sleep() intervals as the game progresses.

Asynchronous Input Mapping: Maps four distinct keyboard interrupts ('Up', 'Down', 'w', 's') to specific paddle instances. This allows for simultaneous two-player interaction without input blocking.

Modular Score State: Integrates a specialized Scoreboard class that manages independent point tallies for the left and right players, triggering a reset_position() sequence whenever a coordinate boundary is breached.
