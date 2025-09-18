import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("istherecorrelation.csv", sep=";", decimal=",")

fig, ax1 = plt.subplots(figsize=(8, 4.5), dpi=300)
ax2 = ax1.twinx()

ax1.plot(df["Year"], df["WO [x1000]"],  label="WO [x1000]")
ax2.plot(df["Year"], df["NL Beer consumption [x1000 hectoliter]"], "y", label="NL Beer [x1000 hl]")

ax1.set_title("Amount of WO students vs. Beer Consumption")
ax1.set_xlabel("Year")
ax1.set_ylabel("WO students [x1000]")
ax2.set_ylabel("Beer [x1000 hl]")
ax1.grid(alpha=0.3)

lines, labels = ax1.get_legend_handles_labels()
l2, lab2 = ax2.get_legend_handles_labels()
ax1.legend(lines + l2, labels + lab2, loc="upper left")

plt.tight_layout()
plt.savefig("plot.png", dpi=300, bbox_inches="tight")
