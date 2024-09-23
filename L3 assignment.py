import polars as pl
import matplotlib.pyplot as plt

df = pl.read_csv("istherecorrelation.csv", truncate_ragged_lines=True, separator=';', decimal_comma=True)

plot = df.plot.line(x="WO [x1000]", y="NL Beer consumption [x1000 hectoliter]")

xdata = df.get_column("Year")
y1data = df.get_column("NL Beer consumption [x1000 hectoliter]")
y2data = df.get_column("WO [x1000]")

plt.rcParams['figure.dpi'] = 300
fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('NL Beer consumption [x1000 hectoliter]', color=color)
ax1.plot(xdata, y1data, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_xlabel('Year', color=color)
ax2.set_ylabel('WO [x1000]', color=color)
ax2. plot(xdata, y2data, color=color)
ax2.tick_params(axis='y', labelcolor=color)


plt.show()