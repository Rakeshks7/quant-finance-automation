# mock_backtest.py
import json
import random
import sys

# Simulate processing time
# time.sleep(2)

def run_backtest():
    # Simulate strategy metrics
    sharpe = round(random.uniform(0.8, 2.5), 2)
    max_dd = round(random.uniform(-5.0, -25.0), 2)
    total_return = round(random.uniform(10.0, 45.0), 2)
    
    results = {
        "status": "success",
        "sharpe_ratio": sharpe,
        "max_drawdown": max_dd,
        "total_return_pct": total_return,
        "trades_executed": random.randint(50, 200)
    }
    
    # Save to JSON file (simulating artifact creation)
    with open('last_run_results.json', 'w') as f:
        json.dump(results, f)
        
    # Print to stdout for n8n to capture immediately
    print(json.dumps(results))

if __name__ == "__main__":
    run_backtest()