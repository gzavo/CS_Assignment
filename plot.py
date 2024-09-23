import matplotlib.pyplot as plt
import polars as pl
import numpy as np

data = pl.read_csv("istherecorrelation.csv", separator=";", decimal_comma=True)

y1 = data["WO [x1000]"]
y2 = data["NL Beer consumption [x1000 hectoliter]"]

# y1 = y1/y1[0] - 1
# y2 = y2/y2[0] - 1
y1g = [ y1[i] / y1[i-1] -1 for i in range(1,len(y1))]
y2g = [ y2[i] / y2[i-1] -1 for i in range(1,len(y1))]

print(np.corrcoef(y1, y2))
print(np.corrcoef(y1g, y2g))

plt.plot(data['Year'][1:], y1g, label="Beer Consumption")
plt.plot(data['Year'][1:], y2g, label = "Number of First-Year Students")
plt.legend()
plt.title("Annual Growth of Beer Consumption vs Number of College Students")
plt.xlabel("Year")

# plt.yscale('log')
plt.savefig("graph.png", dpi=300)
plt.show()