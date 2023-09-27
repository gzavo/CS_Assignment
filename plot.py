"""
This file is created for the assignment for Academic Skills Course and plot the 
"""

import pandas as pd
import os
import matplotlib.pyplot as plt

# Read the file
df = pd.read_csv("istherecorrelation.csv", delimiter=";")
# First few rows
df.head()

# Plot
plt.plot(df["Year"], df["NL Beer consumption [x1000 hectoliter]"])
plt.xlabel("Year")
plt.ylabel("x1000 hectoliters")
plt.title("Beer Consumption in the Netherlands")
plt.savefig("beer.png", dpi=300)

