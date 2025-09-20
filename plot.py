import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('istherecorrelation.csv')

# Load into DataFrame
df = pd.read_csv(StringIO(data_str), sep=";")

# Replace commas with dots for decimals and convert to float
df["WO [x1000]"] = df["WO [x1000]"].str.replace(",", ".").astype(float)

# Plot both variables over time
plt.figure(figsize=(8, 5), dpi=300)
plt.plot(df["Year"], df["WO [x1000]"], marker="o", label="WO [x1000] (university students)")
plt.plot(df["Year"], df["NL Beer consumption [x1000 hectoliter]"], marker="s", label="Beer consumption [x1000 hl]")

plt.xlabel("Year")
plt.ylabel("Values")
plt.title("University Students vs. Beer Consumption in the Netherlands (2006–2018)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Save figure
plot_path = "/mnt/data/correlation_plot.png"
plt.savefig(plot_path, dpi=300)
plt.close()

plot_path
