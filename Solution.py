import matplotlib.pyplot as plt
import csv

with open('istherecorrelation.csv') as file:
    reader = csv.reader(file)
    data = []
    counter = 0
    for lines in reader:
        if counter == 0:
            pass
        else:
            data.append(lines)
        counter +=1

merged_data = []

for inner_list in data:
    merged_inner = ','.join(inner_list).replace(',', '.')
    merged_data.append(merged_inner)

separated_data =[]
for string_element in merged_data:
    elements = string_element.split(';')
    separated_data.extend(elements)

years = []
values1 = []
values2 = []

for inner_list in data:
    year = inner_list[0].split(';')[0]  
    value1 = float(inner_list[0].split(';')[1].replace(',', '.'))
    value2 = float(inner_list[1].split(';')[1].replace(',', '.'))
    years.append(year)
    values1.append(value1)
    values2.append(value2/100)

plt.figure(figsize=(10, 6))
plt.plot(years, values1, label='Value 1 times 1000')
plt.plot(years, values2, label='Value 2 times 100000')
plt.xlabel('Year')
plt.ylabel('Litres of beer and WO consumption')
plt.title('WO and Beer consumption in the Netherlands')
plt.legend()
plt.grid(True)
plt.ylim(0,300)
plt.savefig('correlation_plot.png', dpi=300)

plt.show()