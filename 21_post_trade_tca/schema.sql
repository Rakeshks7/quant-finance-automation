CREATE TABLE IF NOT EXISTS execution_quality_log (
    id SERIAL PRIMARY KEY,
    trade_id VARCHAR(50) NOT NULL,
    ticker VARCHAR(10),
    side VARCHAR(4),             -- 'BUY' or 'SELL'
    exec_price DECIMAL(10, 2),   -- Price you got
    market_midpoint DECIMAL(10, 2), -- Price of the market at that exact second
    slippage_bps DECIMAL(10, 2), -- The difference in Basis Points
    venue VARCHAR(50),           -- Exchange/Broker Name
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);