import csv
from pathlib import Path

import matplotlib.pyplot as plt

data_path = Path("./istherecorrelation.csv")
year = []
wo = []
consumption = []
with data_path.open() as f:
    file = csv.reader(f, delimiter=";")
    next(file)
    for row in file:
        year.append(int(row[0]))
        wo.append(float(row[1].replace(",", ".")))
        consumption.append(int(row[2]))
fig = plt.figure()
axis = fig.subplots(nrows=1)
axis.set_title("A clear correlation between students and beer")
axis.set_xlabel("Year")
axis.set_ylabel("Students (x1000)")
axis.plot(year, wo, label="WO students")
twin = axis.twinx()
twin.set_ylabel("Hectoliter (x1000)")
twin.plot(year, consumption, "r", label="Beer in hectoliter")
lines, labels = axis.get_legend_handles_labels()
lines2, labels2 = twin.get_legend_handles_labels()
twin.legend(lines + lines2, labels + labels2)
fig.tight_layout()
fig.savefig(fname="plot.png", dpi=300)
