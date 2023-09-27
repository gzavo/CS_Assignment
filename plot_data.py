import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data = []
with open("istherecorrelation.csv", "r") as f:
    for line in f.readlines()[1:]:
        line_split = line.strip().split(";")
        line_split[1] = line_split[1].replace(",", ".")
        year, wo, beer = int(line_split[0]), float(line_split[1]), int(line_split[2])
        data.append([year, wo, beer])

data = np.array(data)
years = data[:, 0]
wos = data[:, 1]
beers = data[:, 2]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('YEAR')
ax1.set_ylabel('WO [x1000]', color=color)
ax1.plot(years, wos, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('NL Beer consumption [x1000 hectoliter]', color=color)
ax2.plot(years, beers, color=color)
ax2.tick_params(axis='y', labelcolor=color)

res = np.round(stats.spearmanr(wos, beers).statistic, 4)

plt.title(f"Correlation between WO and NL beer consumption in years 2006-2018\n(Spearman's rank correlation $\sigma = {res}$)")
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig("thereiscorrelation.png", dpi=300)
