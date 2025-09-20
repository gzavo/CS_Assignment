import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    df = pd.read_csv("istherecorrelation.csv", delimiter=";", decimal=",")
    WO = df["WO [x1000]"]
    beer = df["NL Beer consumption [x1000 hectoliter]"]

    fig = plt.figure(dpi=300)
    axes = fig.add_subplot()

    axes.scatter(WO, beer)

    axes.set_title("Netherlands Beer consumption against number of WO")
    axes.set_xlabel("WO [x1000]")
    axes.set_ylabel("Netherlands Beer consumption [x1000 hectoliter]")

    plt.savefig("correlation.png")
