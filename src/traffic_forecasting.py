import pandas as pd
import os

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Load Dataset
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

# Create Frame Number
df["Frame"] = range(len(df))

# Features and Target
X = df[["Frame"]]

y = df["Total"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# Test Prediction
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = mean_squared_error(
    y_test,
    y_pred
) ** 0.5

r2 = r2_score(
    y_test,
    y_pred
)

print("\n===== RANDOM FOREST RESULTS =====\n")

print("MAE :", round(mae, 4))

print("RMSE:", round(rmse, 4))

print("R2  :", round(r2, 4))

# Predict Future Traffic
future_frame = pd.DataFrame({
    "Frame": [len(df) + 1]
})

prediction = model.predict(
    future_frame
)

print(
    "\nPredicted Traffic:",
    int(prediction[0])
)