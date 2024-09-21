import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('istherecorrelation.csv', delimiter=';')
df['WO [x1000]'] = df['WO [x1000]'].str.replace(',', '.').astype(float)
df['NL Beer consumption [x1000 hectoliter]'] = df['NL Beer consumption [x1000 hectoliter]'].astype(float)
df['Beer per Student'] = df['NL Beer consumption [x1000 hectoliter]'] / df['WO [x1000]']

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6), dpi=300)

ax1.plot(df['Year'], df['NL Beer consumption [x1000 hectoliter]'], color='green')
ax1.set_ylabel('NL Beer consumption [x1000 hectoliter]', color='green')
ax1.set_xlabel('Year')

ax1_twin = ax1.twinx()
ax1_twin.plot(df['Year'], df['WO [x1000]'], color='orange')
ax1_twin.set_ylabel('WO [x1000]', color='orange')
ax1.set_title('Correlation with Default Y-Axes')

ax2.plot(df['Year'], df['NL Beer consumption [x1000 hectoliter]'], color='green')
ax2.set_ylabel('NL Beer consumption [x1000 hectoliter]', color='green')
ax2.set_xlabel('Year')
ax2.set_ylim(0, max(df['NL Beer consumption [x1000 hectoliter]']) + 100)

ax2_twin = ax2.twinx()
ax2_twin.plot(df['Year'], df['WO [x1000]'], color='orange')
ax2_twin.set_ylabel('WO [x1000]', color='orange')
ax2_twin.set_ylim(0, max(df['WO [x1000]']) + 10)
ax2.set_title('Correlation with Y-Axes Starting at 0')

ax3.plot(df['Year'], df['Beer per Student'], color='purple', marker='o')
ax3.set_title('Beer Consumption per Student')
ax3.set_xlabel('Year')
ax3.set_ylabel('Beer Consumption per Student (Hectoliters)')

plt.tight_layout()
plt.savefig("correlation.png")
