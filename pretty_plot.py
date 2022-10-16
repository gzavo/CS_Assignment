import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('istherecorrelation.csv', delimiter=';')

data["WO [x1000]"] = data["WO [x1000]"].str.replace(',', '.')
data["WO [x1000]"] = data["WO [x1000]"].apply(pd.to_numeric)
data = data.set_index("Year")


fig = plt.figure(dpi=300)
data.plot.bar(y=[data.columns[0],data.columns[1]])

plt.savefig("plot.png")