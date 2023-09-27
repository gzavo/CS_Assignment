# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import os.path

file = open("/Users/francescocatania/Desktop/istherecorrelation.csv")

list_of_lists = []

next(file)

for i in file:

    lista1 = i.strip(";").split(";")
    lista1[0] = float(lista1[0])
    lista1[1] = float(lista1[1].replace(",", "."))
    lista1[2] = float(lista1[2].replace("\n", " "))
    list_of_lists.append(lista1)
    
array = np.array(list_of_lists)

plt.scatter(array[:,1], array[:,2], color="cornflowerblue")
plt.xlabel("WO Students")
plt.ylabel("Beer consumption [x1000 hectoliter]")
beta, alpha = np.polyfit(array[:,1], array[:,2], 1)
plt.plot(array[:,1], beta * array[:,1] + alpha, color="lightblue")
plt.title("Correlation between WO students and beer consumption in NL")

fig = plt.savefig('/Users/francescocatania/Correlation.png', dpi=300)

fig.savefig('/Users/francescocatania/graph.png')