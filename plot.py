import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot() -> None:
    df = pd.read_csv("istherecorrelation.csv")
    df['NL Beer consumption [x1000 hectoliter]'] = df['NL Beer consumption [x1000 hectoliter]'].apply(lambda x: x/1000)
    df.plot(x="Year", y=["WO [x1000]", "NL Beer consumption [x1000 hectoliter]"],
        subplots=True, layout=(1,2))
    plt.suptitle("Beer consumption")
    plt.ylabel("Beer consumption in hectoliters")
    plt.xlabel("Year")
    plt.show()

if __name__ == "__main__":
    plot()