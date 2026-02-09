🛠 Project 8: Secret AuctionFocus: Dictionary Manipulation & Key-Value Mapping.

🔨 Silent Auction Engine

A secure bidding utility designed to manage high-stakes data ingestion and winner 
determination using hash-map structures.

Data Architecture: Utilizes Python dictionaries to map unique user strings to 
integer-based bid values.

Linear Search Algorithm: Implements a custom iteration loop to traverse the dictionary 
and identify the maximum value, demonstrating foundational knowledge of search patterns 
without relying on built-in max() functions.

Privacy-First UX: Engineered a terminal-clearing mechanism using newline escape sequences to 
maintain "sealed-bid" integrity between different users on a shared interface.

Nested Validation Logic: Employs a dual-layered while loop structure to handle continuous 
data entry and sanitize user responses, preventing program termination on invalid inputs.

State Control: Tracks the lifecycle of the auction through boolean flags (auction_is_active), 
allowing for dynamic session management and a clean exit strategy.