-- Table 1: Your Holdings (FIFO)
CREATE TABLE IF NOT EXISTS trade_ledger (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10),
    buy_date DATE,
    buy_price DECIMAL(10, 2),
    quantity INT,
    status VARCHAR(10) DEFAULT 'OPEN' -- 'OPEN' or 'CLOSED'
);

-- Table 2: The Tax Provision
CREATE TABLE IF NOT EXISTS tax_provision_ledger (
    id SERIAL PRIMARY KEY,
    trade_ref_id INT,
    sell_date DATE,
    realized_gain DECIMAL(15, 2),
    holding_period_days INT,
    tax_type VARCHAR(10),       -- 'STCG' or 'LTCG'
    tax_rate DECIMAL(5, 2),     -- e.g., 0.20 or 0.125
    estimated_tax DECIMAL(15, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);