import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot() -> None:
    """
    Plots the yearly beer consumption of the world vs The Netherlands.
    """
    df = pd.read_csv("istherecorrelation.csv", sep=';', decimal=',')
    df["NL Beer consumption [x1000 hectoliter]"] = df["NL Beer consumption [x1000 hectoliter]"] / 1000
    df.plot(x="Year", y=["WO [x1000]", "NL Beer consumption [x1000 hectoliter]"],
        subplots=True, layout=(1,2))
    plt.suptitle("Beer consumption")
    plt.ylabel("Beer consumption in hectoliters")
    plt.xlabel("Year")
    plt.show()

if __name__ == "__main__":
    plot()
