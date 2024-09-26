import pandas as pd
import matplotlib.pyplot as plt

fname = 'istherecorrelation.csv'
df = pd.read_csv(fname, delimiter=';', decimal=',', names=['y', 'w', 'c'], header=0)

fig, ax1 = plt.subplots(figsize=(7, 4))

ax1.plot(df["y"], df["w"], marker="o", color="blue")
ax1.set_xlabel('Year')
ax1.set_ylabel('WO students (x1000)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue', color='blue')

ax2 = ax1.twinx()
ax2.plot(df["y"], df["c"], marker="o", color="green")
ax2.set_ylabel('Beer consumption (x1000 hectoliter)', color='green')
ax2.tick_params(axis='y', labelcolor='green', color='green')

plt.title('WO enrolments and Beer Consumption through time')

plt.savefig('correlationornot.png', dpi=300)
plt.show()