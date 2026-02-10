🛠 Project 9: Calculator Engine

🔢 Recursive Arithmetic Processor

A dynamic calculation engine designed to handle continuous mathematical operations using function-driven logic and modular design.

Functional Mapping: Implemented a dispatch table (dictionary) that maps arithmetic strings to their corresponding functions. This allows for a clean, extensible architecture where operations are invoked as first-class objects.

Higher-Order Logic: Developed a centralized perform_operations function that abstracts the calculation process, accepting numeric values and operators to return precise results.

Recursive-Style Loop: Engineered a nested while loop system that allows users to "chain" calculations. By passing the result back into the first_number variable, the engine maintains a running total for complex, multi-step operations.

State Persistence: Tracks the calculation session through a continue_calculation flag, enabling a seamless transition between continuing a current operation and flushing the state for a "clean slate" start.

Terminal UX: Incorporates clear-screen logic and ASCII art to maintain a professional, distraction-free CLI environment during fresh calculation resets.