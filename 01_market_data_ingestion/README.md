// This script runs inside the n8n Code Node
const result = items[0].json.chart.result[0];
const quote = result.indicators.quote[0];
const timestamp = result.timestamp[0];

// Create the clean object for SQL insertion
const cleanData = {
  ticker: result.meta.symbol,
  date: new Date(timestamp * 1000).toISOString(),
  open_price: quote.open[0],
  high_price: quote.high[0],
  low_price: quote.low[0],
  close_price: quote.close[0],
  volume: quote.volume[0],
  provider: 'Yahoo Finance'
};

return [{json: cleanData}];