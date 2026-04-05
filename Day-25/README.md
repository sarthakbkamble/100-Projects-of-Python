🛠 Project 23: U.S. States Game

Focus: Data Analysis with Pandas & Coordinate Mapping.

🗺 Interactive Geographic Quiz
A data-driven educational tool that combines graphical mapping with real-time CSV data processing to create an interactive learning experience.

Pandas Data Integration: Leverages the pandas library to ingest and manipulate external .csv datasets. The engine converts raw state data into searchable Python lists and DataFrames for high-speed lookup.

Dynamic Coordinate Plotting: Implemented a system that extracts specific x and y integers from a CSV row and instructs a hidden turtle cursor to navigate to those exact pixel coordinates to label the map.

List Comprehension & Comparison: Features a real-time validation loop that cross-references user input against the all_states list, maintaining a correct_states ledger to track progress and prevent duplicate entries.

Automated "States to Learn" Export: Includes a sophisticated exit sequence. If the user types "Exit," the program utilizes list iteration to identify all missing states and programmatically exports them into a new States_to_learn.csv file using pandas.DataFrame.to_csv().

Stateful UI Updates: Uses f-string integration in the screen.textinput title to provide a live "Score/Total" tracker, enhancing the user experience with immediate feedback on their progress.

Image-to-Coordinate Mapping: Successfully integrates a custom .gif background as a shape, demonstrating the ability to use Turtle as a professional GUI for data visualization projects.