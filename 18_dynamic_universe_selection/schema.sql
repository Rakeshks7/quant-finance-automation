CREATE TABLE IF NOT EXISTS active_universe (
    ticker VARCHAR(10) PRIMARY KEY,
    sector VARCHAR(50),
    market_cap_bn DECIMAL(10, 2),
    avg_volume_30d BIGINT,
    last_updated DATE DEFAULT CURRENT_DATE
);