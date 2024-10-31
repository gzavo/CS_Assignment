import pandas as pd
import numpy as np
import matplotlib
from scipy.optimize import curve_fit

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def extract_data():
    data = pd.read_csv('istherecorrelation.csv', delimiter=';')
    data['WO [x1000]'] = data['WO [x1000]'].str.replace(',', '.').astype(float)
    data['NL Beer consumption [x1000 hectoliter]'] = data['NL Beer consumption [x1000 hectoliter]'].astype(int)
    students = data['WO [x1000]']
    beer_consumption = data['NL Beer consumption [x1000 hectoliter]']
    return students, beer_consumption


def exp_model(x, a, b):
    return a * np.exp(b * x)


students, beer_consumption = extract_data()

slope, intercept = np.polyfit(students, beer_consumption, 1)
linear_trend = slope * students + intercept

params, covariance = curve_fit(exp_model, students, beer_consumption, p0=[1, 0.0001])
a, b = params
exp_trend = exp_model(students, a, b)

fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
ax.scatter(students, beer_consumption, color='blue', label='Data Points')
ax.plot(students, linear_trend, color='red', linestyle='--', label='Linear Trend Line')
ax.plot(students, exp_trend, color='green', linestyle='--', label='Exponential Model Trend Line')
ax.set_title('WO Students vs. Beer Consumption in the Netherlands per year')
ax.set_xlabel('Number of University Students * 10$^3$')
ax.set_ylabel('Beer Consumption * 10$^3$ hectoliters')
ax.grid(True)
ax.legend()
fig.savefig('beer_student_correlation.png', dpi=300)
