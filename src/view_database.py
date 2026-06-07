import sqlite3
import os

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

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM traffic_data"
)

rows = cursor.fetchall()

print("\n===== DATABASE RECORDS =====\n")

for row in rows:
    print(row)

conn.close()