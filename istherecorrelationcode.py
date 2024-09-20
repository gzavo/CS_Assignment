import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr 
plt.style.use('ggplot')

#acces csv data
with open("istherecorrelation.csv") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    #sort data into arrays
    data = list(reader)
    n = len(data)
    years = np.zeros(n)
    WO = np.zeros(n)
    beer_consumption = np.zeros(n)
    
    for i, row in enumerate(data):
        years[i] = int(row[reader.fieldnames[0]])
        WO[i] = float(row[reader.fieldnames[1]].replace(',', '.'))
        beer_consumption[i] = float(row[reader.fieldnames[2]])

#pearson r correlation
correlation, _ = pearsonr(WO, beer_consumption)
print(f"The pearson r correlation is {correlation}.")

#plot of wo students and beer consumption each year and their correlation
fig, axs = plt.subplots(3, figsize=(10, 10))
axs[1].sharex(axs[0])
fig.suptitle("Correlation of WO students and beer consumption")

axs[0].set_ylabel("Beer consumption (x1000 hectoliter)")
axs[0].scatter(years, beer_consumption, c = 'red')

axs[1].set_ylabel("WO students (x1000)")
axs[1].scatter(years, WO,  c = 'blue')
axs[1].set_xlabel("Year")

axs[2].set_ylabel("WO students (x1000)")
axs[2].set_xlabel("Beer consumption (x1000 hectoliter)")
axs[2].scatter(beer_consumption, WO, color='purple')

fig.tight_layout()
plt.savefig('istherecorrelationplot.pdf', dpi=300)
