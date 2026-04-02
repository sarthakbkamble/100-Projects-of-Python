🛠 Project 22: High-Score Snake Engine
Focus: Persistent Data Storage & State Reset Logic.

🐍 Advanced Snake with Persistence
An upgraded version of the classic Snake simulation that introduces permanent data logging to track the "All-Time High Score" even after the program is terminated.

File-Based Persistence: Implements a data-logging system that reads from and writes to a local data.txt file. This allows the high score to persist across different gaming sessions, moving beyond volatile memory.

Non-Destructive Reset Logic: Replaces the standard "Game Over" sequence with a specialized .reset() method. When a collision occurs, the engine updates the high score record and respawns the snake at the origin (0,0) without crashing the application.

Refined Collision Physics: Utilizes scalar distance triggers to detect interactions with food and the snake's own tail. The logic employs list slicing and identity checks (if segment == snake.head: pass) to prevent the head from triggering a self-collision.

Synchronized Render Loop: Uses screen.tracer(0) to disable the default animation delay, allowing for manual frame updates via screen.update(). This ensures the multi-segment body moves as a single cohesive unit.

Global Boundary Constraints: Monitores the snake's Cartesian coordinates against the 600×600 pixel arena. Any movement beyond the ±280 px boundary triggers an automatic state reset and high-score evaluation.

Encapsulated Score Management: The Scoreboard class now handles two distinct integer states—score and high_score—dynamically updating the UI whenever a new record is established.

