
import streamlit as st
from src.fetch_data import get_stock_data
from src.indicators import add_technical_indicators
from src.lstm_model import train_lstm_model
from src.signal_generator import generate_signals
import numpy as np
import pandas as pd
st.title("📈 AI Trading Signal Generator")

ticker = st.text_input("Enter stock ticker", "AAPL")
df = get_stock_data(ticker)
df = add_technical_indicators(df)

st.subheader("Raw Data with Indicators")
st.dataframe(df.tail(20))

model, scaler = train_lstm_model(df)
look_back = 60
latest_data = scaler.transform(df['Close'].values[-look_back:].reshape(-1, 1))
latest_data = np.reshape(latest_data, (1, look_back, 1))
predicted_price = scaler.inverse_transform(model.predict(latest_data))[0][0]

signal = generate_signals(predicted_price, df['Close'].iloc[-1])

st.metric("Predicted Price", f"${predicted_price:.2f}")
current_price = df['Close'].iloc[-1]
if isinstance(current_price, (pd.Series, np.ndarray)):
    current_price = current_price.item()

st.metric("Current Price", f"${current_price:.2f}")

st.metric("Suggested Action", signal)
