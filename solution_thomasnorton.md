* Fantastic yeasts and where to find them: the hidden diversity of dimorphic fungal pathogens
* An analysis of the forces required to drag sheep over various surfaces
* Correlation of continuous cardiac output measured by a pulmonary artery catheter versus impedance cardiography in ventilated patients

![1695851226964](image/solution_thomasnorton/1695851226964.png)


It seems that there is some correlation at the end of the graph, as it follows quite a linear line. However, at the beginning the WO consumption is seems to increase without much of a significant change for the NL Beer consumption. There is also a couple years both values drop.



```python
import matplotlib as plt
import pandas as pd
from scipy.stats import pearsonr


data = pd.read_csv('istherecorrelation.csv', delimiter=';')


year = data['Year']
WO_consumption = pd.to_numeric(data['WO [x1000]'].str.replace(',', '.'))
Beer_consumption = data['NL Beer consumption [x1000 hectoliter]']

correlation_coefficient, _ = pearsonr(WO_consumption, Beer_consumption)

plt.figure( dpi=300)
plt.scatter(WO_consumption, Beer_consumption, marker='o', label='Data Points')
plt.plot(WO_consumption, Beer_consumption, color='red', linestyle='-', linewidth=1, label='Line Connecting Data')
plt.xlabel('WO Consumption [x1000]')
plt.ylabel('NL Beer Consumption [x1000 hectoliter]')
plt.title('Scatter Plot of WO and NL Beer Consumption')

plt.text(210, 11700, f'Correlation: {correlation_coefficient:.2f}', fontsize=12)


plt.legend()
plt.savefig('correlation_scatter_plot_with_line.png')

plt.show()
```
