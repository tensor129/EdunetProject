
def backtest_signals(prices, signals):
    returns = []
    for i in range(1, len(signals)):
        if signals[i-1] == "Buy":
            returns.append((prices[i] - prices[i-1]) / prices[i-1])
        elif signals[i-1] == "Sell":
            returns.append((prices[i-1] - prices[i]) / prices[i-1])
        else:
            returns.append(0)
    return sum(returns)
