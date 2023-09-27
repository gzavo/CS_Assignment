import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("istherecorrelation.csv", delimiter=";")

fig, ax = plt.subplots(figsize=(10, 5), dpi=300)

plt.title("NL Beer consumption and WO per year", fontsize=20)

ax2 = ax.twinx()
ax.plot(data["Year"], data["WO [x1000]"], color='y')
ax2.plot(data["Year"], data["NL Beer consumption [x1000 hectoliter]"], color='r')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('WO [x1000]', color='y', fontsize=12)
ax2.set_ylabel('NL Beer consumption [x1000 hectoliter]', color='r', fontsize=12)
plt.show()
