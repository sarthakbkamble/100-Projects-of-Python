# 🛠 Project: ISS Overhead Notifier

**Focus:** API Parameters, Exception Verification, & Daemon Polling.

## 🛰 Orbital Tracking Dispatcher

A continuous monitoring daemon that queries geographical telemetrics and solar positions simultaneously to determine if the International Space Station is visibly tracking across a specific local vector.

* **Parametric Endpoint Filtering:** Ingests dynamic positional parameters via `requests.get()` to filter remote server queries down to target latitude and longitude configurations.
* **HTTP Status Assurance:** Implements `response.raise_for_status()` to cleanly catch network anomalies or endpoint down-states before attempting buffer reading.
* **ISO 8601 String Parsing:** Splits and isolates strict string datetime stamps (`split("T")`) returned from the solar endpoint to extract atomic integer hour components.
* **Continuous Horizon Verification:** Establishes an infinite daemon loop regulated by a 60-second `time.sleep()` clock throttle, checking target Boolean constraints across multi-factor API conditional splits.

---

Combining multiple API schemas into a automated daemon loop provides the structural groundwork for writing scalable cloud tracking worker nodes.
