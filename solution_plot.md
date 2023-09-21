# Academic Skills Computational Science [5284ASCS6Y]
# L3: Tools for Computational Scientists - Computational Scientist's Toolbox Assignment
# Dan Dong 14989093
# September 21, 2023
# 5. Create one plot from the dataset "istherecorrelation.csv", with DPI=300. The objective is to visualize the data in a way that you consider representative. Include the resulting plot image in the markdown file and add a few lines of interpretation on the data.

# The code part is below:

# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
url = 'https://raw.githubusercontent.com/SuperAileen/CS_Assignment_Dan_Dong_14989093/main/istherecorrelation.csv'

# Load the dataset into a DataFrame
df = pd.read_csv(url, sep=';', header=0, names=['Year', 'WO [x1000]', 'NL Beer consumption [x1000 hectoliter]'])

# # Check the actual column names in the DataFrame
# print(df.columns)

# Create a line plot to visualize the data
plt.figure(figsize=(8, 6))
plt.plot(df['Year'], df['WO [x1000]'], marker='o', linestyle='-', label='Wine&Others Consumption')
plt.plot(df['Year'], df['NL Beer consumption [x1000 hectoliter]'], marker='s', linestyle='--', label='Beer Consumption')
plt.xticks(df['Year'])
plt.xlabel('Year')
plt.ylabel('Consumption')
plt.title('Wine&Others and Beer Consumption Over Time')
plt.legend()

# Display numerical values next to each data point
for i, row in df.iterrows():
    plt.annotate(str(row['NL Beer consumption [x1000 hectoliter]']), (row['Year'], row['NL Beer consumption [x1000 hectoliter]']), textcoords='offset points', xytext=(0,-20), ha='center')

for i, row in df.iterrows():
    plt.annotate(str(row['WO [x1000]']), (row['Year'], row['WO [x1000]']), textcoords='offset points', xytext=(0,10), ha='center')

# Save the plot with DPI=300
plt.savefig('wine&others and beer correlation_plot.png', dpi=300)

# Provide interpretation
print("The plot illustrates the consumption trends of wine and other beverages as well as beer over the years.")
print("Notably, wine and other beverages consumption has exhibited a consistent upward trajectory, while beer consumption has experienced a decline.")
print("This observed pattern hints at a possible negative correlation between wine and other beverages and beer consumption.")
print("However, to substantiate this correlation, further in-depth analysis would be required.")
print("The data is visually presented in the saved plot 'wine&others and beer correlation_plot.png'.")

# Display the plot
plt.show()


![wine&others and beer correlation_plot.png](https://github.com/SuperAileen/CS_Assignment_Dan_Dong_14989093/blob/main/wine%26others%20and%20beer%20correlation_plot.png
)

