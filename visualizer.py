import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the csv data
df = pd.read_csv('istherecorrelation.csv', sep=';')

# Preprocess data
df['WO [x1000]'] = df['WO [x1000]'].str.replace(',', '.').astype(float)
df['NL Beer consumption [x1000 hectoliter]'] = df['NL Beer consumption [x1000 hectoliter]'].astype(float)

# Calculate correlation and create the scatter plot
correlation = df['WO [x1000]'].corr(df['NL Beer consumption [x1000 hectoliter]'])
plt.scatter(df['WO [x1000]'], df['NL Beer consumption [x1000 hectoliter]'], color='blue')

# Fit the polynomial and generate the fit line
coefficients = np.polyfit(df['WO [x1000]'], df['NL Beer consumption [x1000 hectoliter]'], 1)
fit_line = np.poly1d(coefficients)

# Plot the regression line
plt.plot(df['WO [x1000]'], fit_line(df['WO [x1000]']), "r--")

# Add labels and title
plt.xlabel('WO [x1000]')
plt.ylabel('NL Beer consumption [x1000 hectoliter]')
plt.title(f'Correlation: {correlation:.4f}')

# Annotate points on the plot
for i in range(len(df)):
    plt.annotate(df['Year'].iloc[i],
                 (df['WO [x1000]'].iloc[i], df['NL Beer consumption [x1000 hectoliter]'].iloc[i]),
                 fontsize=8, xytext=(5, 5), textcoords='offset points')

plt.tight_layout()

# Save the plot with DPI set to 300
plt.savefig('correlation_plot.png', dpi=300)

# Show the plot
plt.show()
