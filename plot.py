import pandas as pd
import matplotlib.pyplot as plt

# data set of istherecorrelation.csv
data = {
    'Year': [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018],
    'WO [x1000]': [205.9, 208.6, 212.7, 220.5, 233.2, 242.4, 245.4, 241.4, 250.2, 255.7, 261.2, 267.9, 280.1],
    'NL Beer consumption [x1000 hectoliter]': [11402, 11492, 11450, 11502, 11474, 11480, 11452, 11484, 11555, 11601, 11731, 11862, 12048]
}

df = pd.DataFrame(data)
fig, ax1 = plt.subplots()

# axis 1：WO [x1000]
ax1.set_xlabel('Year')
ax1.set_ylabel('WO [x1000]', color='tab:blue')
ax1.plot(df['Year'], df['WO [x1000]'], color='tab:blue', label='WO [x1000]')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# axis 2：NL Beer consumption [x1000 hectoliter]
ax2 = ax1.twinx()
ax2.set_ylabel('NL Beer consumption [x1000 hectoliter]', color='tab:orange')
ax2.plot(df['Year'], df['NL Beer consumption [x1000 hectoliter]'], color='tab:orange', label='Beer Consumption')
ax2.tick_params(axis='y', labelcolor='tab:orange')

plt.title('WO and NL Beer Consumption Over Years')
plt.tight_layout()
plt.savefig("WO_Number_And_NL_Beer_Consumption_from_UvAID_15390802.png", dpi=300)
plt.show()
