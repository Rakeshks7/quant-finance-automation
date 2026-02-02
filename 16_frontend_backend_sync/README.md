#  Frontend-Backend Sync (Signal Dashboard)

A real-time integration pipeline that connects the Python Algorithmic Trading engine to a user-facing React Application.

## Architecture
* **Source:** Python Algorithm (Running on Server).
* **Bridge:** n8n Webhook.
* **Database:** Google Firestore (NoSQL Real-time Database).
* **Notification:** Firebase Cloud Messaging (FCM).

## Workflow Logic
1.  **Trigger:** The Python script generates a buy/sell signal and POSTs the JSON payload to n8n.
2.  **Persistence:** n8n creates a new document in the `trade_signals` Firestore collection.
    * *Note:* Since the React App uses the Firestore SDK, this update is pushed to the UI milliseconds after creation (no page refresh needed).
3.  **Alerting:** n8n uses FCM to send a native Push Notification to the trader's mobile device, ensuring they never miss a trade even if the app is closed.

## Data Structure
The app expects the following JSON payload:
```json
{
  "ticker": "AAPL",
  "action": "BUY",
  "entry_price": 150.00,
  "confidence": 0.9
}