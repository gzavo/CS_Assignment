import pandas as pd
import matplotlib.pyplot as plt

# import data from csv
df = pd.read_csv("istherecorrelation.csv", delimiter = ";")

# set plot parameters
fig, ax = plt.subplots(figsize = (10, 5))
plt.title('Correlation data of students and alcohol usage')

# split data for two y axises
ax2 = ax.twinx()
ax.plot(df["Year"], df["WO [x1000]"], color = 'g')
ax2.plot(df["Year"], df["NL Beer consumption [x1000 hectoliter]"], color = 'b')

# giving labels to the axises
ax.set_xlabel("Years", color = 'r')
ax.set_ylabel("WO [x1000]", color = 'g')
ax.plot(dpi=300)

# secondary y-axis label
ax2.set_ylabel("NL Beer consumption [x1000 hectoliter]", color = 'b')

# defining display layout
plt.tight_layout()

# show plot
plt.show()
plt.savefig("correlation.png")