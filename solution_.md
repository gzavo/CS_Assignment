# Comparison of Graduates (WO) vs Beer Consumption in the Netherlands

## Student Number: 15840417

### References/Valuable Papers:
- MCC Van Dyke et al., 2019
- JT Harvey, Applied Ergonomics, 2002
- DW Ziegler et al., 2005

### Python Code:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("istherecorrelation.csv", delimiter=';', decimal=',')
df.head()
df['Year'] = df['Year'].astype(int)

# Plot with dual y-axes
fig, axis_1 = plt.subplots(figsize=(10, 5), dpi=300)

color = 'tab:red'
axis_1.set_xlabel('Year')
axis_1.set_ylabel('WO [x1000]', color=color)
axis_1.plot(df['Year'], df['WO [x1000]'], color=color, marker='o', label='WO [x1000]')
axis_1.tick_params(axis='y', labelcolor=color)

axis_2 = axis_1.twinx()
color = 'tab:green'
axis_2.set_ylabel('NL Beer consumption [x1000 hectoliter]', color=color)
axis_2.plot(df['Year'], df['NL Beer consumption [x1000 hectoliter]'], color=color, marker='x', label='Beer Consumption')
axis_2.tick_params(axis='y', labelcolor=color)

plt.title('Number of Graduated Students (WO) vs Beer Consumption in NL (2006-2018)')
fig.tight_layout()
plt.show()

fig.savefig('wo_beer_consumption.png', dpi=300)
```
![wo_beer_consumption](https://github.com/user-attachments/assets/983e389b-42d3-4676-a074-cfdeea8c723e)

The graph compares WO (Number of graduates) in the Netherlands (red line) and Beer consumption in hectoliters (green line) from 2006 to 2018.
The number of graduates increased steadily from 2006 to 2018, while beer consumption remained mostly unchanged from 2006 to 2013, after which it had a steady increase.
Hence, no obvious direct correlation between the two variables over time can be deduced, or at least not a strong one.
