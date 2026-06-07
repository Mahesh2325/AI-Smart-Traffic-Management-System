import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_file = os.path.join(BASE_DIR, "results", "traffic_data.csv")

df = pd.read_csv(csv_file)

df["Frame"] = range(len(df))

X = df[["Frame"]]
y = df["Total"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MAE :", mean_absolute_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred) ** 0.5)
print("R2  :", r2_score(y_test, y_pred))
import matplotlib.pyplot as plt

# Plot Actual vs Predicted
plt.figure(figsize=(8, 5))
plt.plot(y_test.values, label="Actual Traffic")
plt.plot(y_pred, label="Predicted Traffic")

plt.title("Actual vs Predicted Traffic")
plt.xlabel("Test Samples")
plt.ylabel("Vehicle Count")
plt.legend()

plt.savefig("results/actual_vs_predicted.png")
plt.show()