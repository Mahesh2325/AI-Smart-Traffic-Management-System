import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load CSV
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_file = os.path.join(
    BASE_DIR,
    "results",
    "traffic_data.csv"
)

df = pd.read_csv(csv_file)

# Use Total vehicles column
data = df["Total"].values.reshape(-1, 1)

# Scale data
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

# Create sequences
X = []
y = []

window_size = 5

for i in range(window_size, len(data_scaled)):
    X.append(data_scaled[i-window_size:i])
    y.append(data_scaled[i])

X = np.array(X)
y = np.array(y)

# Train/Test Split
split = int(len(X) * 0.8)

X_train = X[:split]
X_test = X[split:]

y_train = y[:split]
y_test = y[split:]

# Build LSTM Model
model = Sequential()

model.add(
    LSTM(
        50,
        activation="relu",
        input_shape=(window_size, 1)
    )
)

model.add(Dense(1))

model.compile(
    optimizer="adam",
    loss="mse"
)

# Train Model
history = model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=16,
    validation_data=(X_test, y_test),
    verbose=1
)

# Predictions
predictions = model.predict(X_test)

# Convert Back
predictions = scaler.inverse_transform(predictions)
y_test_actual = scaler.inverse_transform(y_test)

# Metrics
mae = mean_absolute_error(
    y_test_actual,
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        y_test_actual,
        predictions
    )
)

r2 = r2_score(
    y_test_actual,
    predictions
)

print("\n===== LSTM RESULTS =====\n")

print("MAE :", mae)
print("RMSE:", rmse)
print("R2  :", r2)

# ------------------------
# TRAINING LOSS GRAPH
# ------------------------

plt.figure(figsize=(8,5))

plt.plot(
    history.history["loss"],
    label="Training Loss"
)

plt.plot(
    history.history["val_loss"],
    label="Validation Loss"
)

plt.title("LSTM Training Loss")

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.legend()

training_graph = os.path.join(
    BASE_DIR,
    "results",
    "lstm_training.png"
)

plt.savefig(training_graph)

plt.close()

# ------------------------
# ACTUAL VS PREDICTED
# ------------------------

plt.figure(figsize=(8,5))

plt.plot(
    y_test_actual,
    label="Actual"
)

plt.plot(
    predictions,
    label="Predicted"
)

plt.title(
    "LSTM Actual vs Predicted"
)

plt.xlabel("Samples")

plt.ylabel("Vehicle Count")

plt.legend()

prediction_graph = os.path.join(
    BASE_DIR,
    "results",
    "lstm_prediction.png"
)

plt.savefig(
    prediction_graph
)

plt.close()

print("\nGraphs Saved Successfully")

print("Training Graph :", training_graph)

print("Prediction Graph :", prediction_graph)