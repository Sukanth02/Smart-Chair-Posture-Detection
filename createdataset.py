import numpy as np
import pandas as pd

# Create a list of pressure readings for all the 12 features.
pressure_readings = np.random.randint(0, 41, size=(500, 12))

# Create a list of labels.
labels = []
for i in range(500):
    if pressure_readings[i, 0] >= 10 and pressure_readings[i, 0] <= 20:
        labels.append("sitting-healthy")
    elif pressure_readings[i, 0] < 10 or pressure_readings[i, 0] > 20:
        labels.append("sitting-not-healthy")
    else:
        labels.append("not-sitting")

# Create a Pandas DataFrame from the pressure readings and labels.
df = pd.DataFrame({"leftthigh-1": pressure_readings[:, 0],
                   "leftthigh-2": pressure_readings[:, 1],
                   "leftthigh-3": pressure_readings[:, 2],
                   "rightthigh-1": pressure_readings[:, 3],
                   "rightthigh-2": pressure_readings[:, 4],
                   "rightthigh-3": pressure_readings[:, 5],
                   "spine-1": pressure_readings[:, 6],
                   "spine-2": pressure_readings[:, 7],
                   "spine-3": pressure_readings[:, 8],
                   "spine-4": pressure_readings[:, 9],
                   "spine-5": pressure_readings[:, 10],
                   "spine-6": pressure_readings[:, 11],
                   "label": labels})

# Export the DataFrame to a spreadsheet.
df.to_excel("pressure_readings.xlsx", index=False)