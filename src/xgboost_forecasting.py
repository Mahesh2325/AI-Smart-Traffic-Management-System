import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from xgboost import XGBRegressor

# Load CSV
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

# Create frame index
df["Frame"] = range(len(df))

X = df[["Frame"]]
y = df["Total"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train XGBoost
model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, predictions)

rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5

r2 = r2_score(
    y_test,
    predictions
)

print("\n===== XGBOOST RESULTS =====\n")

print("MAE :", mae)
print("RMSE:", rmse)
print("R2  :", r2)