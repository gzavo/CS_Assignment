import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("istherecorrelation.csv", delimiter=";")
print(data)
print(data.columns)



year = data['Year']
wo = data['WO [x1000]'].str.replace(',', '.').astype(float)
beer_cons = data['NL Beer consumption [x1000 hectoliter]'].astype(float)


fig, axs1 = plt.subplots(dpi=300)

axs1.set_xlabel('Year')
axs1.set_ylabel('WO (x1000)', color="blue")
axs1.plot(year, wo, color="blue", marker="o", label="WO")
axs1.tick_params(axis='y', labelcolor="blue")

axs2 = axs1.twinx()
axs2.set_ylabel("NL Beer consumption (x1000)", color="red")
axs2.plot(year, beer_cons, color="red", marker="x", label="Beer consumption")
axs2.tick_params(axis='y', labelcolor='red')

axs1.set_title('WO and Dutch beer consumptions over the years 2006-2018')
fig.tight_layout()
plt.savefig('nocorrelation.png', dpi=300)