# Student number 15840417
# MCC Van Dyke et al., 2019
# JT Harvey, Applied Ergonomics, 2002
# DW Ziegler et al., 2005

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
# Ensure that the file path is correct and delimiter and decimal are set properly
df = pd.read_csv("istherecorrelation.csv", delimiter=';', decimal=',')

df.head()

df['Year'] = df['Year'].astype(int)

# Create a plot with dual y-axes
fig, axis_1 = plt.subplots(figsize=(10, 5), dpi=300)

color = 'tab:red'
axis_1.set_xlabel('Year')
axis_1.set_ylabel('WO [x1000]', color=color)
axis_1.plot(df['Year'], df['WO [x1000]'], color=color, marker='o', label='WO [x1000]')
axis_1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis to plot beer consumption
axis_2 = axis_1.twinx()
color = 'tab:green'
axis_2.set_ylabel('NL Beer consumption [x1000 hectoliter]', color=color)
axis_2.plot(df['Year'], df['NL Beer consumption [x1000 hectoliter]'], color=color, marker='x', label='Beer Consumption')
axis_2.tick_params(axis='y', labelcolor=color)

plt.title('Number of graduated students (WO) vs Beer Consumption in NL (2006-2018)')

fig.tight_layout()
plt.show()
fig.savefig('wo_beer_consumption.png', dpi=300)
