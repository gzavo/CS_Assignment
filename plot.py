# https://www.geeksforgeeks.org/visualize-data-from-csv-file-in-python/

import csv
import matplotlib.pyplot as plt
import numpy as np

year, wo, beer = [], [], []
index=0
with open('istherecorrelation.csv') as File:  
    Line_reader = csv.reader(File, delimiter=';')

    index=0
    for row in Line_reader:
        if index>0:
            year.append(float(row[0]))
            wo.append(float((row[1]).replace(',',''))) # https://stackoverflow.com/questions/6633523/how-can-i-convert-a-string-with-dot-and-comma-into-a-float-in-python
            beer.append(float(row[2]))

        index+=1
  
plt.figure(figsize=[12, 7], dpi=300)
plt.bar(year, beer, color = 'violet')
plt.errorbar(year, beer, yerr=wo, fmt="o", color="lime")
plt.xlabel('Year')
plt.ylabel('NL Beer consumption [x1000 hectoliter]')
plt.title('Beerconsumption over the years')
plt.xticks(np.arange(2006, 2019, 1))
plt.ylim(0,15000)
plt.xlim(2005,2019)
plt.savefig('plot.png')
