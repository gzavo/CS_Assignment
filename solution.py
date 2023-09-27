import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("istherecorrelation.csv", delimiter = ";")
plt.figure(dpi=300)
plt.plot(df["WO [x1000]"], df["NL Beer consumption [x1000 hectoliter]"])
plt.xlabel("WO [x1000]")
plt.ylabel("NL Beer consumption [x1000 hectoliter]")
plt.show()