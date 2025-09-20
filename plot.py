import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('istherecorrelation.csv', sep=";")

# Replace commas with dots for decimals and convert to float
df["WO [x1000]"] = df["WO [x1000]"].str.replace(",", ".").astype(float)


x = df["NL Beer consumption [x1000 hectoliter]"]
y = df["WO [x1000]"]

plt.scatter(x, y)

plt.xlabel("NL Beer consumption (x1000 hectoliter)")
plt.ylabel("University  students (x1000)")
plt.title("Correlation niversity Students and Beer Consumption in the Netherlands")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()



# Save figure
plot_path = "correlation_plot.png"
plt.savefig(plot_path, dpi=300)
plt.close()

plot_path
