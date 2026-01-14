CREATE TABLE IF NOT EXISTS option_chain_history (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    symbol VARCHAR(10) NOT NULL, -- e.g., NIFTY
    expiry_date DATE NOT NULL,
    strike_price DECIMAL(10, 2),
    option_type VARCHAR(2),      -- 'CE' or 'PE'
    ltp DECIMAL(10, 2),          -- Last Traded Price
    oi BIGINT,                   -- Open Interest
    volume BIGINT,
    iv DECIMAL(5, 2)             -- Implied Volatility
);
-- Create an index for faster querying later
CREATE INDEX idx_opt_time ON option_chain_history(timestamp, symbol);