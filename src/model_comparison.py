import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load dataset
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_file = os.path.join(BASE_DIR, "results", "traffic_data.csv")

df = pd.read_csv(csv_file)

# --------------------------
# Random Forest
# --------------------------

df["Frame"] = range(len(df))

X = df[["Frame"]]
y = df["Total"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

# --------------------------
# LSTM
# --------------------------

data = df["Total"].values.reshape(-1, 1)

scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

window_size = 5

X_lstm = []
y_lstm = []

for i in range(window_size, len(data_scaled)):
    X_lstm.append(data_scaled[i-window_size:i])
    y_lstm.append(data_scaled[i])

X_lstm = np.array(X_lstm)
y_lstm = np.array(y_lstm)

split = int(len(X_lstm) * 0.8)

X_train_lstm = X_lstm[:split]
X_test_lstm = X_lstm[split:]

y_train_lstm = y_lstm[:split]
y_test_lstm = y_lstm[split:]

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

model.fit(
    X_train_lstm,
    y_train_lstm,
    epochs=10,
    batch_size=16,
    verbose=0
)

lstm_pred = model.predict(X_test_lstm, verbose=0)

lstm_pred = scaler.inverse_transform(lstm_pred)
y_test_lstm = scaler.inverse_transform(y_test_lstm)

# --------------------------
# Graph
# --------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    range(len(y_test)),
    y_test.values,
    label="Actual"
)

plt.plot(
    range(len(rf_pred)),
    rf_pred,
    label="Random Forest"
)

plt.title("Random Forest vs Actual Traffic")
plt.xlabel("Samples")
plt.ylabel("Vehicle Count")
plt.legend()

output_file = os.path.join(
    BASE_DIR,
    "results",
    "model_comparison.png"
)

plt.savefig(output_file)

plt.show()

print("\nGraph saved successfully!")
print(output_file)