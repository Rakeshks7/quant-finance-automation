# The Master Dashboard (Process 52)

This is the command center for the entire **Fintech Automation Lab**. It connects to the Postgres database and visualizes the outputs of the previous 51 processes.

## How to Run
1.  Navigate to this folder in your terminal.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
4.  Open your browser to `http://localhost:8501`.

## Features
* **Overview:** Real-time P&L and AUM.
* **Strategy:** Visualizes Trend Following (Process 51) and Sector Rotation (Process 45).
* **Risk:** Monitors VaR (Process 23) and Volatility Targeting (Process 50).
* **Execution:** Tracks Slippage (Process 39).
* **Ops:** Checks Reconciliation status (Process 28).

## Note on Data
The dashboard code contains a `get_db_connection()` function. If it cannot connect to your real Postgres database (setup in Process 37), it gracefully falls back to **Mock Data** so you can demo the UI immediately.