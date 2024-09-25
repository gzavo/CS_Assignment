15889378
Fantastic yeasts and where to find them: the hidden diversity of dimorphic fungal pathogens
An analysis of the forces required to drag sheep over various surfaces
The neurocognitive effects of alcohol on adolescents and college students
![Plot Image](https://github.com/IliasSofianos/CS_Assignment/blob/main/download.png)


#CODE FOR THE PLOT

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\elias\\Downloads\\istherecorrelation.csv", sep=';', decimal=',')

plt.figure(dpi=300, figsize=(8, 6))
plt.plot(data['Year'], data['WO [x1000]'], label='WO [x1000]', marker='o')
plt.plot(data['Year'], data['NL Beer consumption [x1000 hectoliter]'], label='Beer Consumption [x1000 hectoliter]', marker='s')

plt.title("WO Graduates and Beer Consumption in NL (2006-2018)")
plt.xlabel("Year")
plt.ylabel("Quantity")
plt.legend()

plt.savefig("correlation_plot.png", dpi=300)

plt.show()

The graph demonstrates the trends of beer consumption and WO graduates during the period 2006 to 2018. The beer consumption exhibits a negligible increase of approximately 5%. The amount of WO graduates displayed a moderate growth of ~20%. There does not appear to be any correlation between the beer consumption and the WO graduates.
