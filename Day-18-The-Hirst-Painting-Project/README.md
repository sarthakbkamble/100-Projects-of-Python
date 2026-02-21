🛠 Project 16: Hirst Painting Generator
Computer Graphics & External Library Integration.

🎨 Algorithmic Art Engine
A generative art utility that utilizes computer vision data to recreate "spot paintings" through automated coordinate plotting and color theory.

Color Extraction & Analysis: Leverages the colorgram library to analyze external JPEG assets, extracting dominant RGB values to build a custom palette for the generative process.

Coordinate Geometry: Implemented precise positional control using the turtle module. The engine utilizes a setheading() and forward() logic pattern to navigate a 2D Cartesian plane without drawing path lines.

Algorithmic Grid Construction: Engineered a 10x10 dot matrix using a single loop and modulo arithmetic (dot_count % 10 == 0). This triggers a row-reset sequence, automating the transition from x-axis progression to y-axis elevation.

RGB Metadata Management: Configured the colormode(255) global state to handle 8-bit color sequences, allowing for high-fidelity reproduction of extracted palette data.

Pseudorandom Aesthetics: Combines the random module with extracted color lists to ensure each execution results in a unique visual arrangement while maintaining a consistent color scheme.