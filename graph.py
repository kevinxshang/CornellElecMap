import glob
import pandas as pd
import matplotlib.pyplot as plt

folder_path = 'CornellElecMap/CornellElec_1.0/datasets/Time_15mins'
files = glob.glob(f'{folder_path}/*.csv')

values = []
for file in files:
    data = pd.read_csv(file)
    electricity_usage = data[data['value'] < 1000]['value'].dropna()
    values.extend(electricity_usage.tolist())

plt.figure(figsize=(10, 6))
plt.hist(values, bins=30, color='blue', edgecolor='black', alpha=0.7)

plt.title('Electricity Usage Distribution', fontsize=16)
plt.xlabel('Electricity Usage (kWh)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

plt.show()