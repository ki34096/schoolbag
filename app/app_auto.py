import pandas as pd
import streamlit as st

st.set_page_config(page_title="Crypto Auto Tracker", page_icon="🪙")

st.title("📈 Crypto Auto Data Viewer")

csv_file = "crypto_data.csv"

try:
    df = pd.read_csv(csv_file)
    st.line_chart(df.set_index("timestamp")[["btc_usd", "eth_usd"]])
    st.dataframe(df)
except FileNotFoundError:
    st.warning("CSV пока не создан. Запусти auto_bot.py.")

