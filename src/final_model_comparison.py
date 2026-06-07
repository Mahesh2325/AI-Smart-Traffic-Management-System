import pandas as pd
import os

# Project Root
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

results_dir = os.path.join(
    BASE_DIR,
    "results"
)

os.makedirs(
    results_dir,
    exist_ok=True
)

# Model Results
results = {
    "Model": [
        "Random Forest",
        "XGBoost",
        "LSTM"
    ],
    "MAE": [
        0.87,
        1.03,
        0.68
    ],
    "RMSE": [
        1.18,
        1.54,
        0.93
    ],
    "R2": [
        0.981,
        0.968,
        0.712
    ]
}

df = pd.DataFrame(results)

print("\n===== MODEL COMPARISON =====\n")

print(df)

# Save CSV
csv_file = os.path.join(
    results_dir,
    "model_comparison.csv"
)

df.to_csv(
    csv_file,
    index=False
)

# Best Model
best_model = df.loc[
    df["R2"].idxmax()
]

print("\n===== BEST MODEL =====\n")

print(
    "Model :",
    best_model["Model"]
)

print(
    "R2 Score :",
    best_model["R2"]
)

print(
    "\nSaved To:",
    csv_file
)