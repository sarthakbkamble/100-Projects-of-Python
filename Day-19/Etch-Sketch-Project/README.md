🛠 Project 17.1: Etch-A-Sketch
Event Listeners & Higher-Order Functions.

🎨 Interactive Sketch Engine
An event-driven input system that maps keyboard interrupts to graphical movement, simulating a digital Etch-A-Sketch interface.

Event-Driven Architecture: Utilizes turtle.listen() to monitor the I/O stream for specific keyboard interrupts, demonstrating an asynchronous control flow where the program responds to real-time user input.

Higher-Order Functions: Employs the onkeypress() method to pass movement functions as arguments, showcasing the ability to treat functions as first-class objects within a listener framework.

State Reset Logic: Implemented a global reset() function that clears the graphics buffer and restores the coordinate pointer to the origin (0,0), effectively "flushing" the application state.

Vector Navigation: Developed discrete movement functions for forward/backward translation and degree-based rotation, allowing for precise user-controlled vector manipulation on a 2D plane.

Functional Encapsulation: Decoupled the movement logic into small, single-purpose functions, adhering to clean code principles and making the mapping of keys to actions highly readable.