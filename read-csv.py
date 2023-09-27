import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

dir = os.path.dirname(os.path.abspath(__file__))

data = pd.read_csv(f"{dir}\istherecorrelation.csv", sep=';', decimal=',')
print(data.columns)

data_wo_beer = data[['WO [x1000]','NL Beer consumption [x1000 hectoliter]']]
data_wo = data['WO [x1000]']
data_beer = data['NL Beer consumption [x1000 hectoliter]']

sns.set_theme()

fig, ax = plt.subplots(2,2,figsize=(10,8))

a = sns.lineplot(data, x='Year', y='WO [x1000]', hue=0, palette=['cornflowerblue'], ax=ax[0,0], legend=False, )
b = sns.lineplot(data, x='Year', y='NL Beer consumption [x1000 hectoliter]', hue=0, palette=['goldenrod'], ax=ax[0,1], legend=False)
c = sns.scatterplot(data, x = 'WO [x1000]', y='NL Beer consumption [x1000 hectoliter]', ax=ax[1,0], legend=False)
d = sns.regplot(data, x = 'WO [x1000]', y='NL Beer consumption [x1000 hectoliter]', ax=ax[1,1])

#corr = data_wo_beer.corr()
#corr = pd.DataFrame.corr(method='callable',data_wo, data_beer)
#heatmap = sns.heatmap(corr, cmap="coolwarm")

plt.suptitle("University Graduates vs. Beer Consumption in the Netherlands")
fig.tight_layout(pad=2.0)

plt.show()