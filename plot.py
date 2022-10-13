from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd

#import data from csv
data = pd.read_csv("istherecorrelation.csv", delimiter=";", decimal=",")

# create figure and axis objects
fig,ax = plt.subplots()

# make a plot
ax.plot(data.iloc[:,0], data.iloc[:,1], color="red", marker="o")

# set x-axis label
ax.set_xlabel("year", fontsize = 14)
# set y-axis label
ax.set_ylabel("WO x1000", color="red", fontsize=14)

# twin object for two different y-axis on the same plot
ax2=ax.twinx()

# make a plot with different y-axis using second axis object
ax2.plot(data.iloc[:,0], data.iloc[:,2],color="blue",marker="o")
ax2.set_ylabel("Beer consumption NL",color="blue",fontsize=14)
plt.show()

#save the plot as a file
fig.savefig('istherecorrelation.jpg', format='jpeg', dpi=300, bbox_inches='tight')

correlation = data.iloc[:,1].corr(data.iloc[:,2])
print(correlation)

