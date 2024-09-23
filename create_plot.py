import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("istherecorrelation.csv", delimiter=';', decimal = ',')

time = data['Year']
wo = pd.to_numeric(data['WO [x1000]'], errors='coerce')/100
beer = pd.to_numeric(data['NL Beer consumption [x1000 hectoliter]'])/10000

plt.figure(figsize=(6, 8), dpi=300)  # Set DPI here
plt.plot(time, wo, color='r', label='WO (*100 000)')
plt.plot(time, beer, color='b', label='NL beer consumption (*10 000 000  hectoliter)')

plt.xlabel('Year')
plt.ylabel('Values')
plt.ylim()
plt.title('WO vs NL Beer Consumption Over Time')
plt.legend(fontsize = 'x-small')

plt.show()
