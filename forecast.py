import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_spending(df):
    df["day"] = range(1, len(df)+1)
    
    X = df[["day"]]
    y = df["amount"]
    
    model = LinearRegression()
    model.fit(X, y)
    
    next_day = np.array([[len(df)+1]])
    prediction = model.predict(next_day)
    
    return prediction[0]