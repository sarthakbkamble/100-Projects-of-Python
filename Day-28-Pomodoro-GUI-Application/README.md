🛠 Project 26: Pomodoro Productivity GUI
Focus: Thread-like Asynchrony & Recursive GUI Updates.

🍅 Time Management Engine
A sophisticated productivity tool that implements the Pomodoro technique using tkinter's event loop to manage complex timing intervals and UI states.

Recursive Callback Mechanism: Utilizes the .after() method to create a non-blocking countdown timer. This allows the GUI to remain responsive while executing recursive function calls every 1,000 milliseconds (1 second).

Stateful Session Logic: Features a reps counter that programmatically shifts the application state between "Work" (25 min), "Short Break" (5 min), and "Long Break" (20 min) using modulo arithmetic.

Canvas Layering: Leverages the Canvas widget to layer dynamic text elements over static images, enabling a custom "Tomato" themed interface with high-fidelity graphical control.

Dynamic String Formatting: Implements mathematical floor division and modulo operators to convert raw seconds into a standardized MM:SS digital clock format, including zero-padding for single-digit values.

Global Timer Control: Manages a my_timer reference to allow for precise execution cancellation via .after_cancel(), facilitating a complete system reset and variable flush.

Visual Progress Tracking: Programmatically updates a check_marks label to display a cumulative "✓" for every completed work session, providing immediate visual feedback on user productivity.