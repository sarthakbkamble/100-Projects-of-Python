# 🛠 Project: Exercise Tracking with Sheety

Focus: Natural Language Processing (NLP), Bearer Token Authentication, & Automated Spreadsheet Ingestion.

🏋️ Workout Telemetry & Spreadsheet Pipeline
An automated fitness telemetry tool that converts natural language input into structured workout metrics via NLP endpoints and posts processed records to a remote spreadsheet using Bearer Token authorization.

NLP Payload Extraction: Sends unstructured natural language strings to an external processing endpoint along with demographic parameters, parsing dynamic metric arrays (exercise name, duration, calorie burn) from JSON responses.

Bearer Token Authorization: Secures outbound RESTful API requests to the database pipeline by passing authorization credentials within custom Authorization: Bearer TOKEN HTTP headers.

Temporal Record Timestamping: Captures system execution time using datetime.now() to format precise date (%d/%m/%Y) and time (%X) stamps for every workout log entry.

Automated Record Insertion: Loops through processed workout payloads and constructs nested JSON payloads to create rows dynamically across remote spreadsheet endpoints.
