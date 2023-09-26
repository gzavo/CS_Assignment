import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("istherecorrelation.csv", sep = ";", header=0)

#data['WO [x1000]'] = pd.to_numeric(data['WO [x1000]'])

plt.figure(dpi=300)
plt.plot(data['Year'], data['NL Beer consumption [x1000 hectoliter]'])
plt.plot(data['Year'], data['WO [x1000]'])
plt.xlabel('Year')
plt.ylabel('NL Beer consumption [x1000 hectoliter]')
plt.title('NL Beer consumption from 2006 - 2018')
plt.show()

## Two y-axis plot
COLOR_CONSUMPTION = "#69b3a2"
COLOR_WO = "#3399e6"

plt.figure(dpi=300)
fig, ax1 = plt.subplots(figsize=(8, 8))
ax2 = ax1.twinx()

ax1.plot(data['Year'], data['NL Beer consumption [x1000 hectoliter]'], color=COLOR_CONSUMPTION, lw=3)
ax2.plot(data['Year'], data['WO [x1000]'], color=COLOR_WO, lw=4)

ax1.set_xlabel("Year")
ax1.set_ylabel("NL Beer consumption [x1000 hectoliter]", fontsize=14)
ax1.tick_params(axis="y")

ax2.set_ylabel("WO [x1000]", fontsize=14)
ax2.tick_params(axis="y")

fig.suptitle("Beer consumption in NL over the years", fontsize=20)
fig.autofmt_xdate()