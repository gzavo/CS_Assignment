# Imports
import pandas as pd
import matplotlib.pyplot as plt

# Read data
data = pd.read_csv('istherecorrelation.csv', sep=';')

# Create figure and twin axes
fig, ax = plt.subplots()
ax2=ax.twinx()

# Plot to axes
ax.plot(data['Year'].values, data['NL Beer consumption [x1000 hectoliter]'].values)
ax2.plot(data['Year'].values, data['WO [x1000]'].values, color='green')

# Labels for axes
ax.set_xlabel("Year")
ax.set_ylabel("NL Beer consumption [x1000 hectoliter]", color="blue")
ax2.set_ylabel("WO [x1000]",color="green")

# Show and save
plt.show()
fig.savefig('istherecorrelation.jpg', dpi=300)
