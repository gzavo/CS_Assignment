import pandas as pd
import matplotlib.pyplot as plt
result = open("results", "w")
f = pd.read_csv("istherecorrelation.csv", header=0, delimiter=";", decimal=",")
df = pd.DataFrame(f)
result.write(str(df.describe()))
result.write("\n")
result.write(str(df.corr()))

ax = plt.figure().add_subplot()
ax.plot(df["Year"], df["NL Beer consumption [x1000 hectoliter]"])
ax.set_xlabel("Year")
ax.set_ylabel("Beer consumption in 1000 hectoliters")
ax.set_title("Trend in Beer Consumption per Year")
plt.savefig("BeerConsumption")
