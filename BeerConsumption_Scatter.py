import pandas as pd
import matplotlib.pyplot as plt

file_path = "istherecorrelation.csv"
df = pd.read_csv(file_path, delimiter=';')
# Loads CSV

WO = 'WO [x1000]'
BEER = 'NL Beer consumption [x1000 hectoliter]'
# Reduce text bloat

df[WO] = df[WO].str.replace(',', '.').astype(float)
# Replace WO commas with dots

fig, ax1 = plt.subplots()
# Initializes figure

plt.scatter(df[WO], 
            df[BEER], 
            color='blue', 
            label='Data Points')
# Create Scatter Plot

plt.xlabel(WO)
plt.ylabel(BEER)
# Plot data

plt.title('Scatter Plot: WO [x1000] vs NL Beer Consumption')
# Give Title

plt.grid(True)
plt.legend()
plt.show()