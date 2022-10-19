import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as scp


with open("istherecorrelation.csv", "r", encoding='utf-8-sig') as csvfile:
    csv_reader =  csv.reader(csvfile)
    i = 0
    values = []
    for row in csv_reader:
        if i == 0:
            titles = row[0].split(';')
            print(titles)
        else:
            values.append(np.array(row[0].split(';'), dtype=float))
        
        i += 1
    data = np.array(values)

    fig = plt.figure()
    fig.suptitle("Correlation between WO and beer consumption in the Netherlands.")

    sub1 = fig.add_subplot(111)
    sub2 = sub1.twinx()

    sub1.scatter(data[:,0], data[:,1], s=15, c='blue')
    sub1.plot(data[:,0], data[:,1], c='blue', label='WO')

    sub2.scatter(data[:,0], data[:,2], s=15, c='orange')
    sub2.plot(data[:,0], data[:,2], c='orange', label='Beer consumption')

    sub2.yaxis.tick_right()
    sub2.yaxis.set_label_position("right")

    sub1.set_xlabel(titles[0])
    sub1.set_ylabel(titles[1])
    sub2.set_ylabel(titles[2])

    # both subplots in one legend
    lns, labels = sub1.get_legend_handles_labels()
    lns2, labels2 = sub2.get_legend_handles_labels()
    sub2.legend(lns + lns2, labels + labels2, loc=0)

    plt.savefig("beer.png", format="png", dpi=300, bbox_inches='tight')

    plt.show()



