import matplotlib.pyplot as plt
import pandas as pd



df= pd.read_csv('istherecorrelation.csv', delimiter = ';')

df["WO [x1000]"] = df["WO [x1000]"].str.replace(',', '.')
df["WO [x1000]"] = df["WO [x1000]"].astype(float)

x = df["Year"]
y1 = df["WO [x1000]"]
y2 = df["NL Beer consumption [x1000 hectoliter]"]
y4 = [i_y2/i_y1 for i_y2, i_y1 in zip(y2, y1)]

width = 0.40

plt.bar(x, y4, width)

plt.xlabel("Years")
plt.ylabel("Times More than World Consumption")
plt.title("Beer Consumption in NL compared to the World")
plt.savefig("plot.png", dpi = 300)