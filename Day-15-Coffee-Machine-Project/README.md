Gemini said
🛠 Project 13: Coffee Machine Simulator
Resource Management & Transactional Logic.

☕ Automated Beverage Engine
A hardware-focused simulation demonstrating complex state monitoring, inventory depletion logic, and multi-currency financial processing.

Dynamic Inventory Tracking: Implemented a resource management system that cross-references a global MENU dictionary against a local resources state. The engine performs real-time validation to ensure hardware requirements are met before initiating a transaction.

Transactional Integrity: Features a multi-step financial processor that converts physical coin counts (pennies, nickels, dimes, quarters) into floating-point dollar values, handling exact-change calculations and refund logic for insufficient funds.

Nested Dictionary Parsing: Demonstrates high-level data extraction by iterating through multi-dimensional dictionaries to dynamically identify and subtract only the specific ingredients required for a selected drink.

Maintainer Access Layer: Engineered "secret" command flags (report, off, balance) to provide administrative oversight, allowing for the inspection of internal machine states and profit margins without disrupting the customer-facing interface.

State Persistence: Manages a continuous execution loop that persists through multiple orders, only terminating when an explicit "off" signal is received, simulating a real-world IoT device lifecycle.