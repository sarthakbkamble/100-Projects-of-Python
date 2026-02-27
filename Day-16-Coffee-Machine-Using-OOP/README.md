🛠 Project 14: OOP Coffee Machine

Object-Oriented Programming (OOP) & Class Abstraction.

☕ Modular Beverage System
A refactored version of the Coffee Machine engine, transitioning from procedural code to a robust Object-Oriented architecture for enhanced scalability and maintenance.

Class Abstraction: Decoupled the monolithic procedural script into three distinct, specialized classes: Menu, CoffeeMaker, and MoneyMachine. This demonstrates a high-level understanding of the "Separation of Concerns" principle.

Object Interaction: Implemented complex communication between objects. The main controller coordinates the data flow—passing a MenuItem object from the Menu to the CoffeeMaker to validate resources and then to the MoneyMachine for payment.

Encapsulation: Leveraged internal class methods like .is_resource_sufficient() and .make_payment() to hide implementation details, exposing only a clean interface for the main program logic.

Attribute Management: Accessed dynamic object attributes (e.g., drink.cost) to handle calculations, moving away from manual dictionary indexing and toward more readable dot-notation syntax.

Scalable Architecture: Designed the system to be "plug-and-play." By using classes, new hardware components or payment methods can be integrated without rewriting the core operational logic.