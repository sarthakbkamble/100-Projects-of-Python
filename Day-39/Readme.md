# 🛠 Project: Flight Deal Finder

Focus: Flight Search API Integration, IATA Code Resolving, & Automated Price Alerts.

✈️ Autonomous Flight Price Monitoring Engine
An automated flight tracking system that retrieves target travel destinations from a Google Sheet database, resolves missing IATA location codes, and searches for low-cost flight deals to trigger notification workflows.

Database Synchronization: Communicates with remote Google Sheets via REST APIs (DataManager) to read destinations and dynamically update missing IATA location codes.

IATA Code Resolution: Queries flight search APIs (FlightSearch) to map city names to official IATA airport identifiers and updates the primary data store.

Parametric Flight Search: Configures multi-variable queries across dynamic date ranges to track round-trip ticket pricing and layover schedules.

Threshold Alert Dispatching: Compares real-time fares against target price thresholds in the database, triggering instant notifications (NotificationManager) when deals are found.
