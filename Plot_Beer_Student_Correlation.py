# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 13:37:19 2021

@author: arong
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

my_data = pd.read_csv('./istherecorrelation.csv',delimiter=";")

year = my_data.Year
students = my_data["WO [x1000]"]
beer = my_data["NL Beer consumption [x1000 hectoliter]"]

students = [float(stu.replace(',', '.')) for stu in students]
beer = [int(be) for be in students]
year = [int(y) for y in year]

perc_student = []
beer_perc = []

for i in range(len(year)-1):
    s = (students[i+1] - students[i])/students[i]*100
    perc_student.append(s)
    b = (beer[i+1] - beer[i])/beer[i]*100
    beer_perc.append(b)

year = year[1:]


plt.rcParams['figure.dpi'] = 300
plt.plot(year, perc_student, 'ro', label='Students')
plt.plot(year, beer_perc, 'bo', label ='Beer')
plt.xlabel('Year')
plt.ylabel('Percentage Change (%)')
plt.legend()
plt.grid()
plt.show()





