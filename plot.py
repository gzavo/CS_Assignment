
import pandas as pd
import matplotlib.pyplot as plt

dt = pd.read_csv('istherecorrelation.csv', delimiter=';')

plt.figure(figsize=(10,8))
plt.plot(dt["Year"], dt["NL Beer consumption [x1000 hectoliter]"])
plt.ylabel("Beer consumption (x 1000 hectoliters)")
plt.xlabel("Year")
plt.title("NL Beer Consumption over the years")

plt.savefig('beerconsumption_plot.png', dpi=300)