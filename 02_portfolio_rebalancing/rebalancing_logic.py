# rebalancing_logic.py
# This logic is embedded inside the n8n Code Node.

def calculate_rebalancing(current_holdings, target_weights, total_cash):
    """
    Calculates the trades needed to align portfolio with target weights.
    """
    portfolio_value = sum([h['value'] for h in current_holdings]) + total_cash
    trades = []

    for target in target_weights:
        ticker = target['ticker']
        target_pct = target['weight']
        
        # Find current holding for this ticker (default to 0)
        current_holding = next((h for h in current_holdings if h['ticker'] == ticker), {'qty': 0, 'value': 0, 'price': 150})
        
        target_value = portfolio_value * target_pct
        current_value = current_holding['value']
        diff_value = target_value - current_value
        
        # Calculate quantity to buy/sell (using current price)
        price = current_holding['price']
        qty_to_trade = int(diff_value / price)
        
        if qty_to_trade != 0:
            action = "BUY" if qty_to_trade > 0 else "SELL"
            trades.append({
                "ticker": ticker,
                "action": action,
                "quantity": abs(qty_to_trade),
                "estimated_value": abs(qty_to_trade * price)
            })
            
    return trades