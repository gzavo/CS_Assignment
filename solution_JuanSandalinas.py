" Importing pandas for dataframe and matplotlib.pypliot for plots"
import pandas as pd
import numpy as np
import scipy.optimize as sciop
import matplotlib.pyplot as plt

"Read the csv file using ; as a delimiter betwen columns"
df = pd.read_csv("istherecorrelation.csv", sep = ";")

" Get columns of year,wo and nl of the data frame as a Series"
years = df.iloc[:, 0].astype(int)
wo = df.iloc[:, 1].str.replace(',','.').astype(float)
nl = df.iloc[:, 2].astype(float)

" Get the correlation betwen wo and nl"

ratio = nl/wo
corr = abs(ratio.corr(years))
print(f'Correlation is {corr}')

" Plotting the correlations per year and setting DPI"
fig, ax1 = plt.subplots(figsize = (10,7)) 
fig.set_dpi(300)
y_ticks = np.arange(40,61,1)

ax1.scatter(years, ratio, label = "Data")
ax1.set_xticks(years)
ax1.set_yticks(y_ticks)

"Adding regression line to the graph"
def linear_function(x, m, n):
    return m * x + n
params,covariance = sciop.curve_fit(linear_function, years, ratio)
m,n = params
y_fit = linear_function(years, m,n)
ax1.plot(years, y_fit, color = "red", label = "Linear fit")

"Adding legend of the graph"
ax1.set_ylabel("Nl/Wo beer consumption")
ax1.set_xlabel("Year")
plt.savefig('Beer.png', dpi=300) 






