import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("istherecorrelation.csv", delimiter = ";")

plt.figure(dpi=300)
plt.plot(data["Year"], data["WO [x1000]"])
plt.xlabel("Year")
plt.ylabel("WO [x1000]")
plt.title("WO [x1000] per year")
plt.show()

plt.figure(dpi=300)
plt.plot(data["Year"], data["NL Beer consumption [x1000 hectoliter]"])
plt.xlabel("Year")
plt.ylabel("NL Beer consumption [x1000 hectoliter]")
plt.title("NL Beer consumption [x1000 hectoliter] per year")
plt.show()