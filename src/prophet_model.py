
from prophet import Prophet
import pandas as pd

def forecast_with_prophet(df):
    df_prophet = df[['Close']].reset_index().rename(columns={'Date': 'ds', 'Close': 'y'})
    model = Prophet()
    model.fit(df_prophet)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    return forecast
