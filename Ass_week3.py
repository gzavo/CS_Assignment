import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('istherecorrelation.csv', sep=';')

fig, ax1 = plt.subplots()

ax1.plot(df['Year'], df['NL Beer consumption [x1000 hectoliter]'], color='red')
ax1.set_xlabel('Year')
ax1.set_ylabel('Beer consumption [x1000 Hectoliter]')

ax2 = ax1.twinx()
ax2.scatter(df['Year'], df['WO [x1000]'])

ax2.set_ylabel('WO [x1000]')

fig.savefig('Beerplot', dpi=300)
plt.show()
