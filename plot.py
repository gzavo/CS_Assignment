import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'istherecorrelation.csv'  # Update with the actual path if needed
data = pd.read_csv(file_path, delimiter=';')

# Clean the data by replacing commas with dots and converting to numeric types
data['WO [x1000]'] = data['WO [x1000]'].str.replace(',', '.').astype(float)
data['NL Beer consumption [x1000 hectoliter]'] = data['NL Beer consumption [x1000 hectoliter]'].astype(int)

# Create a figure and axis with DPI=300
fig, ax1 = plt.subplots(figsize=(10, 6), dpi=300)

# Plot WO [x1000] on the first y-axis
ax1.set_xlabel('Year')
ax1.set_ylabel('WO [x1000]', color='tab:blue')
ax1.plot(data['Year'], data['WO [x1000]'], label='WO [x1000]', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis for beer consumption
ax2 = ax1.twinx()
ax2.set_ylabel('NL Beer consumption [x1000 hectoliter]', color='tab:green')
ax2.plot(data['Year'], data['NL Beer consumption [x1000 hectoliter]'], label='NL Beer consumption', color='tab:green')
ax2.tick_params(axis='y', labelcolor='tab:green')

# Add a title and a grid for better readability
plt.title('WO [x1000] vs NL Beer Consumption Over Time')
fig.tight_layout()
plt.grid(True)

# Save the figure
plt.savefig('wo_vs_beer_consumption.png')

# Show the plot
plt.show()
