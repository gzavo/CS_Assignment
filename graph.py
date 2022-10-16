from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('istherecorrelation.csv', delimiter = ';')

data["WO [x1000]"] = data["WO [x1000]"].str.replace(',', '.')
data["WO [x1000]"] = data["WO [x1000]"].astype(float)

print("\nCorrelation------------")
print(data.corr())
print("\nMean-------------------")
print(data.mean())
print("\nStandard Deviation------")
print(data.std())

dataFrame1 = pd.DataFrame({
        'Year': data["Year"],
        'WO': data["WO [x1000]"]
    })

dataFrame2 = pd.DataFrame({
        'Year': data["Year"],
        'NL_Beer': data["NL Beer consumption [x1000 hectoliter]"]
    })

fig,ax = plt.subplots(figsize=(20, 9))

ax.plot(dataFrame1.Year, dataFrame1.WO, color='steelblue', marker='.', label='WO [x1000]')
ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel('WO [x1000]', color='steelblue', fontsize=16)
ax.set_title('Change in WO and Beer Consumption ~ 2006-2018', fontsize=16)
ax.legend(loc=2)

ax2 = ax.twinx()
ax2.plot(dataFrame2.Year, dataFrame2.NL_Beer, color='red', marker='.', label= 'NL Beer consumption [x1000 hectoliter]')
ax2.set_ylabel('NL Beer consumption [x1000 hectoliter]', color='red', fontsize=16)
ax2.legend(loc=4)

# plt.show()
plt.savefig('graph.png', dpi = 300)
