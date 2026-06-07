import streamlit as st
import sqlite3
import pandas as pd
import os

st.title("Smart Traffic Database Dashboard")

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

db_path = os.path.join(
    BASE_DIR,
    "database",
    "traffic.db"
)

conn = sqlite3.connect(db_path)

df = pd.read_sql_query(
    "SELECT * FROM traffic_data",
    conn
)

st.dataframe(df)

st.subheader("Traffic Statistics")

st.write(
    "Average Vehicles:",
    df["vehicle_count"].mean()
)

st.write(
    "Average Speed:",
    df["avg_speed"].mean()
)

conn.close()