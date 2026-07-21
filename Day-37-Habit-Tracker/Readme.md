# 🛠 Project: Habit Tracking Pixel Graph

**Focus:** Custom Header Authentication, RESTful CRUD Mapping, & Date String Formatting.

📊 Habit Telemetry Engine
A quantitative habit-tracking client application that interacts with the Pixela API to dynamically generate, post, update, and remove scalar daily habit metrics using clean RESTful verb patterns.

**Header-Based Authentication:** Transmits security credentials via custom HTTP header structures (`X-USER-TOKEN`), isolating secret token transport away from core request parameters.
**RESTful CRUD Patterning:** Maps application logic against standard HTTP verbs (`POST` for node creation, `PUT` for updates, `DELETE` for purging) across parameterized REST endpoints.
**Temporal String Formatting:** Utilizes `datetime.strftime("%Y%m%d")` to dynamically convert live system clock instances into strict date-stamped URL path parameters.
**Dynamic Quantity Injection:** Ingests interactive user CLI inputs directly into JSON payload payloads, enabling dynamic daily data posting without requiring code updates.

---

Implementing strict RESTful HTTP verbs combined with header token authentication provides the underlying foundation for modern API client architectures.
