import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "istherecorrelation.csv"
df = pd.read_csv(file_path, delimiter=';')
# Loads CSV

WO = 'WO [x1000]'
WO_RATE = 'WO Rate'
BEER = 'NL Beer consumption [x1000 hectoliter]'
BEER_RATE = 'Beer Consumption Rate'
BLUE = 'tab:blue'
RED = 'tab:red'

df[WO] = df[WO].str.replace(',', '.').astype(float)
# Replace WO commas with dots

df[WO_RATE] = df[WO].diff()
df[BEER_RATE] = df[BEER].diff()
# Calculate rate of change

fig, ax1 = plt.subplots()
# Initializes figure

ax1.set_xlabel('Year')
# Labels X-axis

ax1.set_ylabel(WO_RATE, 
               color='tab:blue')
# Labels left y-axis

ax1.plot(df['Year'], 
         df[WO_RATE], 
         label=WO_RATE, 
         color='tab:blue', 
         marker='o')
# Plots WO in left y-axis

ax2 = ax1.twinx()
# Creates twin y-axis on right side

ax2.set_ylabel(BEER_RATE, 
               color='tab:red')
# Labels right y-axis

ax2.plot(df['Year'], 
         df[BEER_RATE], 
         label=BEER_RATE, 
         color='tab:red', 
         marker='o')
# Plots NL Beer Consumption on right y-axis

plt.title('WO Rate and NL Beer Consumption Rate')
# Add Title

plt.grid(True)
# Add grid

plt.show()