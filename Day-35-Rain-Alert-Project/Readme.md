# 🛠 Project: Automated Rain Alert Notifier

**Focus:** Environment Variable Security, Weather API Integration, & Twilio WhatsApp Gateway.

## 🌧 Telemetric Rain Warning System

An automated atmospheric monitoring script that queries predictive multi-hour meteorological forecasts and triggers instant SMS/WhatsApp alerts via a third-party gateway when moisture thresholds are exceeded.

* **Environment Variable Isolation:** Leverages the `dotenv` module and `os.environ.get()` to securely retrieve critical system keys without hardcoding access tokens directly into version control.
* **Granular Forecast Slicing:** Passes a strict count constraint (`"cnt": 4`) within the API request parameters to bound the predictive weather data matrix to an immediate 12-hour forecast window.
* **Condition Code Classification:** Implements an evaluation check (`weather["weather id"] < 700`) to isolate specific meteorological phenomena, successfully matching precipitation codes while filtering out clear sky states.
* **WhatsApp Gateway Integration:** instantiates a secure communication channel via Twilio's REST client architecture (`Client`), dispatching formatted string payloads to specialized sandbox recipient destinations.

---

Abstracting credential layers into environment profiles while handling third-party communication pipelines provides a foundation for robust, cloud-ready backend alerts.
