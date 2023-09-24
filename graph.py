# 0. Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1. Data

data = pd.read_csv('istherecorrelation.csv', delimiter=';')
x = data['WO [x1000]'].str.replace(',', '.').astype(float)
y = data['NL Beer consumption [x1000 hectoliter]'].astype(float)

# check if x and y are of same length
n = len(x)
if n != len(y):
    raise ValueError('x and y must be of same length')

# 2. Calculate Pearson correlation coefficient
pearson_correlation_coefficient = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / \
                                  np.sqrt((n * np.sum(x**2) - np.sum(x)**2) * 
                                          (n * np.sum(y**2) - np.sum(y)**2))

# 3. Plot

plt.figure(figsize=(10, 5), dpi=300)
plt.scatter(x,y)
plt.xlabel('WO [x1000]')
plt.ylabel('NL Beer consumption [x1000 hectoliter]')
plt.title(' between WO students vs. beer consumption')
plt.figtext(0.2, 0.7, 'Pearson correlation coefficient = %f' % pearson_correlation_coefficient)
plt.savefig('plot.png')
plt.show()
