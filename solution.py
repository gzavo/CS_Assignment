import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd

df = pd.read_csv("istherecorrelation.csv") 

years = []
for year in df.index:
    years.append(int(year[:4]))
values = []
for value in df.values:
    values.append(int(value[0][2:]))
fit = np.polyval(np.polyfit(years,values, 2), years)
plt.plot(years, values, 'b.')
plt.plot(years, fit)
plt.show()