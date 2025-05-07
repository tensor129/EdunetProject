import pandas as pd
import numpy as np

def generate_signals(predicted_price, current_price):
    # Ensure both are float scalars, not Series
    if isinstance(predicted_price, (pd.Series, np.ndarray)):
        predicted_price = predicted_price.item()
    if isinstance(current_price, (pd.Series, np.ndarray)):
        current_price = current_price.item()

    change = (predicted_price - current_price) / current_price

    if change > 0.02:
        return "Buy"
    elif change < -0.02:
        return "Sell"
    else:
        return "Hold"
