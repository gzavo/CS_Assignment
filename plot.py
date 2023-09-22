import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('istherecorrelation.csv', delimiter=';', decimal=",")
print(data)

x = np.array(data['Year'])

y = np.array(data['WO [x1000]'])
print(x)

z = np.array(data['NL Beer consumption [x1000 hectoliter]'])
print(y)

b, a = np.polyfit(y, z, 1)

# Create a representative plot
plt.figure(dpi=300)
plt.scatter(y, z)
plt.plot(y, a + b*y)

plt.xlabel('WO [x1000]')
plt.ylabel('NL Beer consumption [x1000 hectoliter]')
plt.title('Correlation Between WO and NL Beer Consumption')
plt.grid(True)

# Save the plot as an image
plt.savefig('correlation_plot.png', dpi=300)