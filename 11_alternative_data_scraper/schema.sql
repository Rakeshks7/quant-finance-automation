CREATE TABLE IF NOT EXISTS alt_data_metrics (
    id SERIAL PRIMARY KEY,
    event_date DATE NOT NULL,
    category VARCHAR(50),       -- e.g., 'F1_RACE', 'WEATHER_BRAZIL'
    metric_name VARCHAR(100),   -- e.g., 'Winning_Constructor', 'Rainfall_mm'
    metric_value TEXT,          -- Stored as text to handle names or numbers
    raw_source VARCHAR(255),    -- URL where data came from
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);