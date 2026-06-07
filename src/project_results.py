import pandas as pd
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

csv_file = os.path.join(
    BASE_DIR,
    "results",
    "traffic_data.csv"
)

df = pd.read_csv(csv_file)

print("\n===== PROJECT RESULTS =====\n")

avg_vehicles = round(
    df["Total"].mean(),
    2
)

max_vehicles = df["Total"].max()

min_vehicles = df["Total"].min()

print("Average Vehicles :", avg_vehicles)
print("Maximum Vehicles :", max_vehicles)
print("Minimum Vehicles :", min_vehicles)

print("\nDensity Distribution")

density_counts = df["Density"].value_counts()

report = []

report.append("===== TRAFFIC ANALYTICS REPORT =====\n")

report.append(
    f"Average Vehicles : {avg_vehicles}"
)

report.append(
    f"Maximum Vehicles : {max_vehicles}"
)

report.append(
    f"Minimum Vehicles : {min_vehicles}"
)

report.append("\nDensity Distribution")

for density, count in density_counts.items():

    percentage = (
        count / len(df)
    ) * 100

    line = (
        f"{density}: "
        f"{percentage:.2f}%"
    )

    print(line)

    report.append(line)

# Save Report
report_file = os.path.join(
    BASE_DIR,
    "results",
    "analytics_report.txt"
)

with open(
    report_file,
    "w"
) as file:

    for line in report:
        file.write(line + "\n")

print(
    "\nReport Saved:"
)

print(report_file)