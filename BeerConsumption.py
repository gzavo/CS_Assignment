import pandas as pd
import matplotlib.pyplot as plt

file_path = "istherecorrelation.csv"
df = pd.read_csv(file_path, delimiter=';')
# Loads CSV

WO = 'WO [x1000]'
BEER = 'NL Beer consumption [x1000 hectoliter]'
BLUE = 'tab:blue'
RED = 'tab:red'
# Reduce text bloat

df[WO] = df[WO].str.replace(',', '.').astype(float)
# Replace WO commas with dots

fig, ax1 = plt.subplots()
# Initializes figure

ax1.set_xlabel('Year')
# Labels X-axis

ax1.set_ylabel(WO, 
               color=BLUE)
# Labels left y-axis

ax1.plot(df['Year'], 
         df[WO], 
         label=WO, 
         color=BLUE, 
         marker='o')
# Plots WO in left y-axis

ax2 = ax1.twinx()
# Creates twin y-axis on right side

ax2.set_ylabel(BEER, 
               color=RED)
# Labels right y-axis

ax2.plot(df['Year'], 
         df[BEER], 
         label=BEER, 
         color=RED, 
         marker='o')
# Plots NL Beer Consumption on right y-axis

plt.title('WO [x1000] and NL Beer Consumption Over Years')
# Add Title

plt.grid(True)
# Add grid

plt.show()