from src.loader import load_data
from src.categorizer import category_summary
from src.anomaly import detect_anomalies
from src.forecast import forecast_spending

def run_finance_ai():
    df = load_data()
    
    summary = category_summary(df)
    anomalies = detect_anomalies(df)
    forecast = forecast_spending(df)
    
    return df, summary, anomalies, forecast