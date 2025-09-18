import pandas as pd
import matplotlib.pyplot as plt

# Read CSV (semicolon separated, and commas as decimal separator)
df = pd.read_csv("istherecorrelation.csv", sep=";", decimal=",")

# Create plot
fig, ax1 = plt.subplots(figsize=(8,5))

# WO (number of students)
ax1.plot(df["Year"], df["WO [x1000]"], "b-o", label="WO students [x1000]")
ax1.set_xlabel("Year")
ax1.set_ylabel("WO students [x1000]", color="b")
ax1.tick_params(axis="y", labelcolor="b")

# Beer consumption
ax2 = ax1.twinx()
ax2.plot(df["Year"], df["NL Beer consumption [x1000 hectoliter]"], "r-s", label="Beer consumption [x1000 hl]")
ax2.set_ylabel("Beer consumption [x1000 hl]", color="r")
ax2.tick_params(axis="y", labelcolor="r")

# Title and layout
plt.title("University Students vs Beer Consumption in NL")
fig.tight_layout()

# Save high-resolution plot
plt.savefig("students_vs_beer.png", dpi=300)

plt.show()