import csv
import matplotlib.pyplot as plt

# Read data from CSV file
with open('istherecorrelation.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    data = list(reader)

# Read titles from first row
titles = data[0]
# Separate data from years, WO and Beer on ;'

years = [int(row[0]) for row in data[1:]]
WO = [float(row[1].replace(',', '.')) for row in data[1:]]
Beer = [float(row[2].replace(',', '.')) for row in data[1:]]


# Plot data
fig, ax1 = plt.subplots()
ax1.plot(years, WO, 'b-')
ax1.set_xlabel('Year')
ax1.set_ylabel('WO [x1000]', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(years, Beer, 'r-')
ax2.set_ylabel('Beer consumption [x1000 hectoliter]', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.show()
# fig.savefig('beer.svg', format='svg', dpi=300)
