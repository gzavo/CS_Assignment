import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("istherecorrelation.csv", delimiter = ";")

fig, ax = plt.subplots(figsize = (10, 5), dpi=300)

plt.title("NL Beer consumption and WO students per year", fontsize=6)
 
ax2 = ax.twinx()
ax.plot(data["Year"], data["WO [x1000]"], color = 'g')
ax2.plot(data["Year"], data["NL Beer consumption [x1000 hectoliter]"], color = 'b')
 
ax.set_xlabel('Year', fontsize=6)
ax.set_ylabel('WO [x1000]', color = 'g', fontsize=6)

ax2.set_ylabel('NL Beer consumption [x1000 hectoliter]', color = 'b', fontsize=6)
plt.show()