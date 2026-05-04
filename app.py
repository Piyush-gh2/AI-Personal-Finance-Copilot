import streamlit as st
import pandas as pd
from src.agents import run_finance_ai
from src.rag import load_knowledge, build_index, retrieve

st.title("💰 AI Personal Finance Copilot")

query = st.text_input("Ask Financial Advice")

if st.button("Analyze Finances"):
    
    df, summary, anomalies, forecast = run_finance_ai()
    
    st.subheader("📊 Transactions")
    st.dataframe(df)
    
    st.subheader("📊 Category Spending")
    st.bar_chart(summary)
    
    st.subheader("⚠️ Anomalies")
    st.write(anomalies)
    
    st.subheader("📈 Forecast")
    st.write(f"Next Spending Prediction: {forecast:.2f}")
    
    # RAG
    docs = load_knowledge()
    index = build_index(docs)
    
    if query:
        insights = retrieve(query, docs, index)
        st.subheader("🔎 Financial Advice")
        for i in insights:
            st.write(i)