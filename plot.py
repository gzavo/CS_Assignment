import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('istherecorrelation.csv', sep = ';')
df['WO [x1000]'] = df['WO [x1000]'].map(lambda x : float(x.replace(',', '.')))
#df = df.drop('Year', axis = 1)
corr = df.corr()
print(corr)
#ax = sns.heatmap(corr)

sns.lineplot(data = df, x = 'Year', y = 'WO [x1000]', color = 'r')
ax2 = plt.twinx()
sns.lineplot(data = df, x = 'Year', y = 'NL Beer consumption [x1000 hectoliter]', ax = ax2)


plt.title('correlation between WO and NL beer consumption')
#plt.show()
plt.savefig('corr.png', dpi=300)
