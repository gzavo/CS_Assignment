import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import pearsonr

# load the data, using the correct delimiters and decimal format
df = pd.read_csv('istherecorrelation.csv', delimiter=';', decimal=',', dtype=float)

# setting up a figure and two y-axes for the plot
fig, ax1 = plt.subplots(figsize=(8, 6), dpi=300)

# creating a secondary axis to plot the second variable (beer consumption)
ax2 = ax1.twinx()
# setting the range for the secondary y-axis (beer consumption)
ax2.set_ylim(11300, 12100)

# plot the student numbers on the primary y-axis
ax1.plot(df.iloc[:, 0], df.iloc[:, 1], label='WO student numbers', c='b')
# plot the beer consumption on the secondary y-axis
ax2.plot(df.iloc[:, 0], df.iloc[:, 2], label='Beer Consumption', c='r')

# labeling the axes based on the column names
ax1.set_xlabel(df.columns[0])
ax1.set_ylabel(df.columns[1])
ax2.set_ylabel(df.columns[2])

# adding a legend and positioning it
fig.legend(loc='upper right', bbox_to_anchor=(0.37, 0.985), bbox_transform=ax1.transAxes)

# adding gridlines for better readability
plt.grid()

# saving the first plot (line plot)
plt.savefig('linegraph')

# calculating the Pearson correlation coefficient between student numbers and beer consumption
pearson_corr, _ = pearsonr(df.iloc[:, 1], df.iloc[:, 2])

# defining the linear function to fit the data (beer consumption vs student numbers)
def func(x, alpha, beta):
    return alpha + beta * x

# fitting the data to the linear function using curve_fit
popt, pcov = curve_fit(func, df.iloc[:, 1], df.iloc[:, 2])
a_opt, b_opt = popt

# generating x values for the linear fit
x = np.linspace(201, 290, 300)

# setting up a new figure for the scatter plot and fitted line
fig = plt.figure(figsize=(8, 6), dpi=300)

# plotting the linear fit based on optimized parameters
plt.plot(x, func(x, a_opt, b_opt), c='steelblue')

# scatter plot of the original data points (student numbers vs beer consumption)
plt.scatter(df.iloc[:, 1], df.iloc[:, 2], c='r')

# setting labels for the axes
plt.xlabel(df.columns[1])
plt.ylabel(df.columns[2])

# setting x and y axis limits
plt.xlim([201, 290])
plt.ylim([11300, 12100])

# adding gridlines again
plt.grid()

# saving the second plot (correlation plot)
plt.savefig('correlation')

# printing the Pearson correlation coefficient
print(f"Pearson Correlation Coefficient: R={pearson_corr:.4f}")
