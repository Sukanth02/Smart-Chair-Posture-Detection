import random
import pandas as pd

# Define the labels and their corresponding conditions
def assign_label(left_thigh, right_thigh, spine):
    thigh_range = [10 <= pressure <= 20 for pressure in left_thigh] + [10 <= pressure <= 20 for pressure in right_thigh]
    spine_range = [10 <= pressure <= 20 for pressure in spine]
    if thigh_range.count(True) >= 2 and spine_range.count(True) >= 2:
        return "sitting-not-healthy"
    elif thigh_range.count(True) == 6 and spine_range.count(True) == 0:
        return "please-lean-back"
    elif all(pressure == 0 for pressure in left_thigh + right_thigh + spine):
        return "not-sitting"
    else:
        return "sitting-healthy"

# Create an empty DataFrame
data = pd.DataFrame(columns=[
    "leftthigh-1", "leftthigh-2", "leftthigh-3",
    "rightthigh-1", "rightthigh-2", "rightthigh-3",
    "spine-1", "spine-2", "spine-3", "spine-4", "spine-5", "spine-6",
    "Label"
])

# Generate 500 random samples
samples = []

for _ in range(500):
    sample = {
        "leftthigh-1": random.randint(0, 40),
        "leftthigh-2": random.randint(0, 40),
        "leftthigh-3": random.randint(0, 40),
        "rightthigh-1": random.randint(0, 40),
        "rightthigh-2": random.randint(0, 40),
        "rightthigh-3": random.randint(0, 40),
        "spine-1": random.randint(0, 40),
        "spine-2": random.randint(0, 40),
        "spine-3": random.randint(0, 40),
        "spine-4": random.randint(0, 40),
        "spine-5": random.randint(0, 40),
        "spine-6": random.randint(0, 40),
    }

    label = assign_label(
        [sample[f"leftthigh-{i}"] for i in range(1, 4)],
        [sample[f"rightthigh-{i}"] for i in range(1, 4)],
        [sample[f"spine-{i}"] for i in range(1, 7)]
    )

    sample["Label"] = label
    samples.append(sample)

# Add more data samples specifically for "not-sitting" and "please-lean-back"
for _ in range(100):
    sample = {
        "leftthigh-1": 0,
        "leftthigh-2": 0,
        "leftthigh-3": 0,
        "rightthigh-1": 0,
        "rightthigh-2": 0,
        "rightthigh-3": 0,
        "spine-1": 0,
        "spine-2": 0,
        "spine-3": 0,
        "spine-4": 0,
        "spine-5": 0,
        "spine-6": 0,
        "Label": "not-sitting"
    }
    samples.append(sample)

for _ in range(100):
    sample = {
        "leftthigh-1": random.randint(10, 20),
        "leftthigh-2": random.randint(10, 20),
        "leftthigh-3": random.randint(10, 20),
        "rightthigh-1": random.randint(10, 20),
        "rightthigh-2": random.randint(10, 20),
        "rightthigh-3": random.randint(10, 20),
        "spine-1": 0,
        "spine-2": 0,
        "spine-3": 0,
        "spine-4": 0,
        "spine-5": 0,
        "spine-6": 0,
        "Label": "please-lean-back"
    }
    samples.append(sample)

# Shuffle the data samples randomly
random.shuffle(samples)

data = pd.concat([data, pd.DataFrame(samples)], ignore_index=True)

# Save the dataset to a CSV file
data.to_csv("smart_chair_dataset.csv", index=False)
