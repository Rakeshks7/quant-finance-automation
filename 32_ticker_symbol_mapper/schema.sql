CREATE TABLE IF NOT EXISTS symbol_map (
    current_ticker VARCHAR(10) NOT NULL, -- e.g., META
    previous_ticker VARCHAR(10),         -- e.g., FB
    exchange VARCHAR(10),                -- e.g., NASDAQ
    change_date DATE,                    -- When the rename happened
    is_active BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (current_ticker, previous_ticker)
);

-- Example Seed Data
INSERT INTO symbol_map (current_ticker, previous_ticker, exchange, change_date) 
VALUES ('META', 'FB', 'NASDAQ', '2022-06-09');