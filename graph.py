import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('CornellElec_1.0/datasets/Time_15mins/Cleaned_BaileyHall.csv')

electricity_usage = data['value']

plt.figure(figsize=(10, 6))
plt.hist(electricity_usage, bins=30, color='blue', edgecolor='black', alpha=0.7)

plt.title('Electricity Usage Distribution', fontsize=16)
plt.xlabel('Electricity Usage (e.g., kWh)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

plt.show()