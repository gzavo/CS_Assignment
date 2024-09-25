import pandas as pd
import matplotlib.pyplot as plt

file_path = 'istherecorrelation.csv'
df = pd.read_csv(file_path, sep=';')

fig, ax1 = plt.subplots(figsize=(10, 5))

color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('WO [x1000]', color=color)
ax1.plot(df['Year'], df['WO [x1000]'], marker='o', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True)

ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('NL Beer Consumption [x1000 hl]', color=color)
ax2.plot(df['Year'], df['NL Beer consumption [x1000 hectoliter]'], marker='s', color=color)
ax2.tick_params(axis='y', labelcolor=color)

ax1.set_title('WO Enrollments & NL Beer Consumption Over the Years')
fig.tight_layout() 

plt.savefig('Correlation_Plot.png', dpi=300)  
plt.show()
