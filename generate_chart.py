import polars as pl
import matplotlib.pyplot as plt
import seaborn as sns

#Load file
df = pl.read_csv("istherecorrelation.csv",separator=';')

#Convert to correct types and clean up files
df = df.with_columns([
    pl.col('Year').cast(pl.Int32),
    pl.col('WO [x1000]').str.replace(',','.').cast(pl.Float64),
    pl.col('NL Beer consumption [x1000 hectoliter]').cast(pl.Float64)
])

# Calculate correlation
correlation = df.select([
    pl.corr('WO [x1000]', 'NL Beer consumption [x1000 hectoliter]').alias('correlation')
]).to_pandas().iloc[0]['correlation']

# Graph in a plot
plt.figure(figsize=(8, 6))
sns.regplot(x='WO [x1000]', y='NL Beer consumption [x1000 hectoliter]', data=df, scatter_kws={'alpha':0.5})
plt.title('Correlation between WO [x1000] and NL Beer Consumption')
plt.xlabel('WO [x1000]')
plt.ylabel('NL Beer consumption [x1000 hectoliter]')
plt.text(0.05, 0.95, f'Correlation: {correlation:.2f}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.5))
plt.tight_layout()
plt.show()