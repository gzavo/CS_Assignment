# Importing the required libraries
import matplotlib.pyplot as plt
import pandas as pd

# Read the data
data = pd.read_csv("istherecorrelation.csv", delimiter=';',decimal=',')

# Create figure and twin axes
#data.plot(x="Year", y=["WO [x1000]", "NL Beer consumption [x1000 hectoliter]"])

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('WO [x1000]', color=color)
ax1.plot(data['Year'], data['WO [x1000]'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Beer consumption', color=color)  # we already handled the x-label with ax1
ax2.plot(data['Year'], data['NL Beer consumption [x1000 hectoliter]'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

#Save the plot
fig.savefig('istherecorrelation.jpg', dpi=300)
