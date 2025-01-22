class Strategy:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.position = 0

    def rsi_strategy(self, price_data, rsi_threshold=30):
        # Example RSI strategy
        if price_data['RSI'] < rsi_threshold:
            return "BUY"
        elif price_data['RSI'] > (100 - rsi_threshold):
            return "SELL"
        return "HOLD"

    def execute_trade(self, signal, price):
        if signal == "BUY" and self.balance > price:
            self.position += 1
            self.balance -= price
            return f"Bought 1 unit at {price}"
        elif signal == "SELL" and self.position > 0:
            self.position -= 1
            self.balance += price
            return f"Sold 1 unit at {price}"
        return "No trade executed."
