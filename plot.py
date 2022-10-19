import pandas as pd
from matplotlib import pyplot as plt
from tabulate import tabulate

plt.rcParams["figure.autolayout"] = True
plt.rcParams['figure.dpi'] = 300
df = pd.read_csv("istherecorrelation.csv")

# displaying the DataFrame
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

# create figure and axis objects with subplots()
fig,ax = plt.subplots()
# make a plot
ax.plot(df["Year"],
        df["WO [x1000]"],
        color="red", 
        marker="o")
# set x-axis label
ax.set_xlabel("year", fontsize = 14)
# set y-axis label
ax.set_ylabel("WO [x1000]",
              color="red",
              fontsize=6)

# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(df["Year"], df["NL Beer consumption [x1000 hectoliter]"],color="blue",marker="o")
ax2.set_ylabel("NL Beer consumption [x1000 hectoliter]",color="blue",fontsize=6)
plt.show()
# save the plot as a file
fig.savefig('plot.png',
            format='jpeg',
            dpi=300,
            bbox_inches='tight')