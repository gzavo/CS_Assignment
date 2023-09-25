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

# Get the current Axes
ax1 = plt.gca() 
df['WO [x1000]'] = df['WO [x1000]'].str.replace(',', '.').astype(float)   # Replace comma with dot and convert to float
ax1.plot(df['Year'], df['WO [x1000]'], marker='o', linestyle='-', color='dodgerblue', label='Number of People with WO Education')
ax1.set_ylabel('Number of People with WO Education [x1000]', color='dodgerblue')
ax1.tick_params(axis='y', labelcolor='dodgerblue')
ax1.set_xlabel('Year')
plt.xticks(df['Year'], rotation=45) 
ax1.set_title('Correlation between WO Education and Beer Consumption in NL')

# Create a second Y axis on the right
ax2 = ax1.twinx()
df['NL Beer consumption [x1000 hectoliter]'] = df['NL Beer consumption [x1000 hectoliter]'].astype(int)
ax2.plot(df['Year'], df['NL Beer consumption [x1000 hectoliter]'], marker='s', linestyle='--', color = 'orange', label='Beer Consumption')
ax2.set_ylabel('NL Beer Consumption [x1000 hectoliter]', color = 'orange')
ax2.tick_params(axis='y', labelcolor = 'orange')

# Display numerical values next to each data point
for i, row in df.iterrows():
    ax1.annotate(str(row['WO [x1000]']), (row['Year'], row['WO [x1000]']), textcoords='offset points', xytext=(0,10), ha='center')
    
for i, row in df.iterrows():
    ax2.annotate(str(row['NL Beer consumption [x1000 hectoliter]']), (row['Year'], row['NL Beer consumption [x1000 hectoliter]']), textcoords='offset points', xytext=(0,-20), ha='center')

# Save the plot with DPI=300
plt.savefig('Correlation between WO Education and Beer Consumption in NL', dpi=300)

# Provide interpretation
print("This graph illustrates changing trends in WO education and beer consumption in the Netherlands between 2006 and 2018. ")
print("From the figure, we can observe that while the number of WO-educated individuals steadily increased, beer consumption experienced continuous fluctuations from 2006 to 2012, followed by sustained growth after 2012. ")
print("The inverse relationship over the first six years may suggest that as the number of WO-educated students increased, they were more likely to opt for alternative beverages instead of beer, contributing to the decline in beer consumption. ")
print("Conversely, the changes in the last six years may indicate that people with a WO education have become more receptive to beer. As the number of individuals with a WO education continued to rise during this period, beer sales also increased year by year. ")
print("However, it's important to note that correlation does not imply causation. Further investigation would be necessary to determine if there is a direct relationship or if other factors are influencing these trends. ")
print("The data is visually presented in the saved plot 'Correlation between WO Education and Beer Consumption in NL.png'. ")

# Display the plot
plt.show()


![Correlation between WO Education and Beer Consumption in NL.png](https://github.com/SuperAileen/CS_Assignment_Dan_Dong_14989093/blob/main/Correlation%20between%20WO%20Education%20and%20Beer%20Consumption%20in%20NL.png)
