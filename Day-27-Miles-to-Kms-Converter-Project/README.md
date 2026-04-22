🛠 Project 25: Mile to Km Converter
Focus: Graphical User Interface (GUI) Development with Tkinter.

📐 Precision Conversion Interface
A desktop application that utilizes the tkinter library to provide a functional, event-driven interface for unit conversions.

GUI Window Orchestration: Configures a master Tk() window with specific dimensions and internal padding (padx/pady) to ensure a clean, professional aesthetic.

Grid Geometry Management: Employs the .grid() layout manager to precisely position labels, entries, and buttons within a coordinate system (columns and rows), demonstrating control over UI alignment.

Dynamic State Updating: Features a convert() function that captures string data from an Entry widget, performs a float conversion and mathematical calculation (miles×1.609344), and dynamically updates a Label component with the result.

Event-Driven Programming: Utilizes the command attribute in the Button widget to bind user click events to the conversion logic, creating a responsive application flow.

Input Handling: Implements an Entry widget for data ingestion, using default value insertion (.insert(END, string="0")) to guide user interaction and prevent null-value errors.

Mainloop Execution: Manages the application's lifecycle via window.mainloop(), which listens for events and keeps the interface active until manually closed by the user.