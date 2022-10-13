import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("istherecorrelation.csv", sep = ";", decimal =",", header = 0, names = ["Year", "WO", "Beer consumption"])#, index_col = 0)
data["WO"] = data["WO"].astype('float')
print(data.head())
# print(data.iloc[1])


ax = data.plot(x="Year", y="WO", legend=False)
ax2 = ax.twinx()
data.plot(x="Year", y="Beer consumption", ax=ax2, legend=False, color="r")
ax.set_ylabel("WO x 1000")
ax2.set_ylabel("Beer consumption x 1000 hectoliter ")
plt.title("Beer consumption and WO over time")
ax.figure.legend()
plt.savefig('plot.png', dpi=300)
