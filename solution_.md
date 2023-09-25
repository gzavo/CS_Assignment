Fantastic yeasts and where to find them: the hidden diversity of dimorphic fungal pathogens
MCC Van Dyke et al., 2019

An analysis of the forces required to drag sheep over various surfaces
JT Harvey, Applied Ergonomics, 2002

The neurocognitive effects of alcohol on adolescents and college students
DW Ziegler et al., 2005

import pandas as pd
import matplotlib.pyplot as plt
data="C:\\Users\\Sheng\\Downloads\\istherecorrelation.csv"
df = pd.read_csv(data,delimiter=";")
plt.figure(figsize=(8, 4),dpi=300)
x = df.iloc[:, 0]
y = df.iloc[:, 2]
plt.plot(x, y)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('NL Beer Consumption Over Years')
plt.show()
![](NL Beer Consumption.png)
From 2006 to 2018, the annual consumption of beer in the Netherlands has generally shown an upward trend.However, after 2012, the growth rate accelerated much more significantly.
