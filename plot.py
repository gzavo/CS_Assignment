"""Plot some beer data.
Author: Robbie Koevoets BSc
UvAnetID: 12855537
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def read_data(filename):
    return pd.read_csv(filename, delimiter=';', decimal=',')


def plot_beer_data(data):
    year_vals, _, consumption_vals = data.T.values

    plt.figure()

    plt.plot(year_vals, consumption_vals)

    plt.title("Beer consumption in the Netherlands")
    plt.xlabel("Year")
    plt.ylabel("Consumption (x1000 hectoliter)")

    with open("plot.png", "wb") as fp:
        plt.savefig(fp)
    plt.show()


if __name__ == "__main__":
    plt.rcParams["figure.dpi"] = 300
    plt.rcParams["savefig.dpi"] = 300

    plot_beer_data(read_data("istherecorrelation.csv"))
