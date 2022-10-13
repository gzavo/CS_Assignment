import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('istherecorrelation.csv', sep = ';', decimal=',')
data = pd.DataFrame(data)

ax = plt.subplot()

# fig.subplots_adjust(right=0.88)
twin = ax.twinx()

p1, = ax.plot(data['Year'],data['WO [x1000]'],'r-',label='WO [x1000]')
p2, = twin.plot(data['Year'],data['NL Beer consumption [x1000 hectoliter]'],'b-',label='NL Beer consumption [x1000 hectoliter]')

tkw = dict(size=4, width=1.5)
ax.tick_params(axis='y', colors=p1.get_color(), **tkw)
twin.tick_params(axis='y', colors=p2.get_color(), **tkw)
ax.tick_params(axis='x', **tkw)

ax.legend(handles=[p1, p2])

plt.show()

plt.savefig('plot.png')