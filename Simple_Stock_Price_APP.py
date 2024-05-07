import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Stock App for APPLE
""")

tickerSymbol = "AAPL"
tickerData = yf.Ticker(tickerSymbol)
tickerDF = tickerData.history(period='id', start='2010-5-31', end='2024-5-4')

st.write("""
## Closing Price
""")
st.line_chart(tickerDF.Close)

st.write("""
## Volume Price
""")

st.line_chart(tickerDF.Volume)

st.write("""
# Stock App for Google
""")

tickerSymbol = "GOOGL"
tickerData = yf.Ticker(tickerSymbol)
tickerDF = tickerData.history(period='id', start='2010-5-31', end='2024-5-4')

st.write("""
## Closing Price
""")
st.line_chart(tickerDF.Close)

st.write("""
## Volume Price
""")

st.line_chart(tickerDF.Volume)