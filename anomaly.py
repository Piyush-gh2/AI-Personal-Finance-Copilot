def detect_anomalies(df):
    avg = df["amount"].mean()
    anomalies = df[df["amount"] > avg * 2]
    return anomalies