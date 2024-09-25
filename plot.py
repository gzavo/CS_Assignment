import csv
import matplotlib.pyplot as plt


# Read the CSV data.
time = []
a = []
b = []
with open('istherecorrelation.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)
    for row in reader:
        time.append(row[0])
        # Replace the comma with a dot to be able to read as float.
        a.append(float(row[1].replace(',', '.')))
        b.append(float(row[2].replace(',', '.')))

# set subplot size
fig, ax1 = plt.subplots(dpi=300, figsize=(10, 5))

# subplot 1 for wo students
ax1.set_xlabel('Years')
ax1.set_ylabel('Amount of WO students [x1000]', color='blue')
ax1.plot(time, a, color='blue', marker='s', label='Students')
ax1.tick_params(axis='y', labelcolor='blue')

# subplot 2 for beer consumption
ax2 = ax1.twinx()
ax2.set_ylabel('Amount of beer consumed [x1000 hL]', color='red')
ax2.plot(time, b, color='red', marker='o', label='Beer consumtion')
ax2.tick_params(axis='y', labelcolor='red')

# Setup the legend of the lines
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0)

# safe the plot as plot.png
plt.title('Correlation between beer consumption and WO students in the Netherlands')
plt.savefig('plot.png')
