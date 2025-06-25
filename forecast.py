import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


# Using a simple linear regression model to predict the next day's energy usage based on historical data

def predict_next_day():

    df = pd.read_csv('data/energy_usage.csv')
    
    df['day'] = np.arange(len(df))
    X = df[['day']]
    y = df['usage_kWh']

    model = LinearRegression()
    model.fit(X, y)

    next_Day = [[len(df)]]
    predicition = model.predict(next_Day)

    return predicition[0]

if __name__ == "__main__":
    next_day_usage = predict_next_day()
    print(f"Predicted energy usage for the next day: {next_day_usage:.2f} kWh")    