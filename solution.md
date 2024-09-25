# Student number 15840417
# MCC Van Dyke et al., 2019
# JT Harvey, Applied Ergonomics, 2002
# DW Ziegler et al., 2005

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('istherecorrelation.csv', delimiter=';', decimal=',')
data['Year'] = data['Year'].astype(int)
fig, ax1 = plt.subplots(figsize=(10, 6), dpi=300)
color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('WO [x1000]', color=color)
ax1.plot(data['Year'], data['WO [x1000]'], color=color, marker='o', label='WO [x1000]')
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('NL Beer consumption [x1000 hectoliter]', color=color)
ax2.plot(data['Year'], data['NL Beer consumption [x1000 hectoliter]'], color=color, marker='x', label='Beer Consumption')
ax2.tick_params(axis='y', labelcolor=color)
plt.title('Comparison of WO and Beer Consumption in NL (2006-2018)')

fig.tight_layout()
plt.show()

fig.savefig('wo_beer_consumption.png', dpi=300)
