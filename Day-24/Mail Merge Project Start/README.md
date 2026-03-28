🛠 Project 24: Mail Merge Automator
Focus: File I/O Systems & String Buffer Manipulation.

✉️ Automated Document Generator
A high-efficiency scripting utility designed to handle batch document processing by merging template buffers with external data streams.

File Stream Management: Utilizes Python's with statement to ensure safe file handling, automatically managing the opening and closing of I/O streams for both the "starting letter" template and the "invited names" data source.

String Sanitization: Implements the .strip() method to clean newline characters (\n) and whitespace from the input name list, ensuring file naming conventions remain valid and professional.

Dynamic Content Injection: Employs the .replace() method to perform precise string substitution within the template buffer, swapping the [name] placeholder for active variables in the iteration loop.

Automated File Serialization: Features a dynamic write-loop that generates unique output files for each record using f-string formatting (letter_for_{name}). This automates the creation of a personalized "ReadyToSend" directory.

Relative vs. Absolute Path Logic: Demonstrates the ability to navigate complex directory structures to locate inputs and define output destinations across different storage volumes.