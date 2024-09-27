import pandas as pd
import matplotlib.pyplot as plt

dt = pd.read_csv('istherecorrelation.csv', delimiter=';')
dt.columns = ["year", "wox1000", "nl_beerx1000"]
dt['wox1000'] = dt['wox1000'].str.replace(',', '.').astype(float)

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel('Year')
ax1.set_ylabel('WO Beer Consumption (x1000 hectoliters)', color='tab:blue')
ax1.plot(dt['year'], dt['wox1000'], marker='o', color='tab:blue', label='WO Beer Consumption')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('NL Beer Consumption (x1000 hectoliters)', color='tab:orange')
ax2.plot(dt['year'], dt['nl_beerx1000'], marker='s', color='tab:orange', label='NL Beer Consumption')
ax2.tick_params(axis='y', labelcolor='tab:orange')

plt.title('WO vs NL Beer Consumption Over the Years')
ax1.grid(True)

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

plt.savefig('beerconsumption_plot.png', dpi=300)