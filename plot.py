import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('istherecorrelation.csv', delimiter=';')
data['WO [x1000]'] = data['WO [x1000]'].str.replace(',', '.').astype(float)
data['NL Beer consumption [x1000 hectoliter]'] = data['NL Beer consumption [x1000 hectoliter]'].astype(float)

# Plot with separate y-axes
fig, ax1 = plt.subplots(figsize=(10, 6), dpi=300)

# Beer Consumption on the left
ax1.plot(data['Year'], data['NL Beer consumption [x1000 hectoliter]'], label='NL Beer Consumption [x1000 hl]', color='blue', marker='o')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('NL Beer Consumption [x1000 hl]', color='blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')

# WO on the right
ax2 = ax1.twinx()
ax2.plot(data['Year'], data['WO [x1000]'], label='WO [x1000]', color='orange', marker='s')
ax2.set_ylabel('WO [x1000]', color='orange', fontsize=12)
ax2.tick_params(axis='y', labelcolor='orange')

# Add title and grid
plt.title('WO Growth vs NL Beer Consumption (2006-2018)', fontsize=14)
fig.tight_layout()

# Save  plot
plt.savefig('plot.png')

# Get correlation
correlation_value = data['WO [x1000]'].corr(data['NL Beer consumption [x1000 hectoliter]'])
print(correlation_value)