🛠 Project 27: Password Manager GUI
Focus: Secure Data Serialization & Clipboard Integration.

🔐 Encrypted Credential Vault
A high-utility desktop application that automates complex password generation and provides a localized storage solution for sensitive credentials.

List Comprehension & Randomization: Features a robust generate_password() function utilizing nested list comprehensions and the random module to create unpredictable strings containing a mix of alphanumeric characters and symbols.

Clipboard Automation: Integrates the pyperclip library to automatically copy the newly generated password to the user's system clipboard, streamlining the "copy-paste" workflow for account registration.

Dialog Box Management: Implements the messagebox module to handle user validation sequences. This includes showinfo for field-validation warnings and askokcancel for verifying data before final persistence.

Persistent Text Logging: Employs a file-handling loop to append (mode="a") formatted credentials—website, username, and password—into a localized data.txt file, ensuring data survives application restarts.

Advanced Grid Geometry: Demonstrates mastery of tkinter grid management by using columnspan and the sticky="ew" attribute to create a modern, responsive layout where entry widgets span multiple columns.

UI Focus & Defaulting: Optimizes the user experience by setting an initial cursor focus (.focus()) on the website field and pre-populating a standard email address using the .insert() method.