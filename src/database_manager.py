import sqlite3
import os
import pandas as pd

# Project Root
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Database Path
db_path = os.path.join(
    BASE_DIR,
    "database",
    "traffic.db"
)

# CSV Path
csv_file = os.path.join(
    BASE_DIR,
    "results",
    "traffic_data.csv"
)

# Connect Database
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS traffic_data (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    vehicle_count INTEGER,

    density TEXT,

    avg_speed REAL,

    signal_decision TEXT

)
""")

# Read Latest Traffic Data
df = pd.read_csv(csv_file)

latest = df.iloc[-1]

vehicle_count = int(latest["Total"])

density = str(latest["Density"])

# Simple Speed Estimation
avg_speed = round(
    max(
        10,
        60 - vehicle_count
    ),
    2
)

# Signal Decision
if vehicle_count > 30:

    signal_decision = "Road A Green"

else:

    signal_decision = "Road B Green"

# Insert Record
cursor.execute("""
INSERT INTO traffic_data (

    vehicle_count,
    density,
    avg_speed,
    signal_decision

)
VALUES (?, ?, ?, ?)
""",
(
    vehicle_count,
    density,
    avg_speed,
    signal_decision
))

conn.commit()

print("\n===== DATABASE UPDATED =====\n")

print("Vehicle Count :", vehicle_count)

print("Density       :", density)

print("Average Speed :", avg_speed)

print("Signal        :", signal_decision)

conn.close()