import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_file = os.path.join(
    BASE_DIR,
    "results",
    "traffic_data.csv"
)

df = pd.read_csv(csv_file)

print("\n===== TRAFFIC ANALYTICS REPORT =====\n")

# Vehicle Statistics
print("Total Records:", len(df))

print("Average Vehicles:",
      round(df["Total"].mean(), 2))

print("Maximum Vehicles:",
      df["Total"].max())

print("Minimum Vehicles:",
      df["Total"].min())

# Density Statistics
print("\nDensity Distribution")

density_counts = df["Density"].value_counts()

for density, count in density_counts.items():

    percentage = (count / len(df)) * 100

    print(
        f"{density}: {percentage:.2f}%"
    )

# Congestion Level
avg_traffic = df["Total"].mean()

if avg_traffic < 15:
    congestion = "LOW"

elif avg_traffic < 30:
    congestion = "MEDIUM"

else:
    congestion = "HIGH"

print("\nOverall Congestion Level:",
      congestion)

print("\n===== END OF REPORT =====")