import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data file
df = pd.read_csv("istherecorrelation.csv", sep=";")

# Renaming columns
df.rename(columns=
	{'WO [x1000]': 'WO_Count', 
	'NL Beer consumption [x1000 hectoliter]': 'Beer_Consumption'}, 
	inplace=True)

# Convert string data in csv to numeric (floating point numbers)
df['WO_Count'] = df['WO_Count'].str.replace(',', '.').astype(float)
df['Beer_Consumption'] = df['Beer_Consumption'].astype(int)

# Create figure
plt.figure(figsize=(8, 6))

# Create a scatter plot with a trend line
sns.regplot(data=df, x='WO_Count', y='Beer_Consumption', marker='o', color='blue', line_kws={'color': 'red'})

# Adding titles and labels
plt.title('WO Admissions vs NL Beer Consumption')
plt.xlabel('WO (in 1000 students)')
plt.ylabel('NL Beer consumption (in 1000 hectoliters)')
plt.grid()

# Save the plot with DPI = 300
plt.savefig('solution_plot.png', dpi=300)

# Show the plot
plt.show()



