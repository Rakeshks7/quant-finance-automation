#  Quant Infrastructure Setup

This folder contains the Infrastructure-as-Code (IaC) to run the Fintech Automation Lab. It builds a custom n8n instance capable of running heavy quantitative Python scripts.

## Why is this needed?
Standard n8n does not come with `pandas` or `scikit-learn`. Without this custom Docker setup, all your "Code Nodes" from previous modules will fail.

## Installation Steps
1.  **Install Docker Desktop** on your machine.
2.  Open terminal in this folder.
3.  Run:
    ```bash
    docker-compose up -d --build
    ```
4.  Open your browser to `http://localhost:5678`.
5.  **Import** the workflow JSON files from the other 36 folders.

## Dependencies Included
* **Python 3.11**
* **Pandas/Numpy:** For matrix math and data manipulation.
* **Statsmodels:** For Cointegration and ADF tests.
* **Postgres:** For the Trade Ledger and historical data.