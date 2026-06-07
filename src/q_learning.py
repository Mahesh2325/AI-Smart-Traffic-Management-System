import random
import pandas as pd
import os

# Q Table
Q = {
    0: [0, 0],
    1: [0, 0]
}

alpha = 0.1
gamma = 0.9

for episode in range(1000):

    north = random.randint(5, 50)
    south = random.randint(5, 50)
    east = random.randint(5, 50)
    west = random.randint(5, 50)

    state = 0 if (north + south) > (east + west) else 1

    action = random.choice([0, 1])

    waiting_ns = east + west
    waiting_ew = north + south

    if action == 0:
        reward = -waiting_ns
    else:
        reward = -waiting_ew

    old_value = Q[state][action]

    Q[state][action] = old_value + 0.1 * (
        reward + 0.9 * max(Q[state]) - old_value
    )

print("\n===== Q LEARNING RESULTS =====\n")

print("Learned Q Table:")
print(Q)

# Test Scenario
north = 42
south = 35
east = 15
west = 18

state = 0 if (north + south) > (east + west) else 1

best_action = Q[state].index(
    max(Q[state])
)

if best_action == 0:

    signal = "North-South GREEN"

    green_time = 45

else:

    signal = "East-West GREEN"

    green_time = 45

print("\n===== SIGNAL DECISION =====\n")

print("North :", north)
print("South :", south)
print("East  :", east)
print("West  :", west)

print("\nDecision :", signal)
print("Green Time :", green_time)

# Save Results
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

results_file = os.path.join(
    BASE_DIR,
    "results",
    "q_learning_results.csv"
)

df = pd.DataFrame({
    "North": [north],
    "South": [south],
    "East": [east],
    "West": [west],
    "Signal": [signal],
    "Green_Time": [green_time]
})

df.to_csv(
    results_file,
    index=False
)

print("\nResults Saved:")
print(results_file)