import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = "./istherecorrelation.csv"
df_from_csv = pd.read_csv(csv_file_path, sep=';', decimal=',')

df_from_csv['WO [x1000]'] = pd.to_numeric(df_from_csv['WO [x1000]'], errors='coerce')
df_from_csv['NL Beer consumption [x1000 hectoliter]'] = pd.to_numeric(df_from_csv['NL Beer consumption [x1000 hectoliter]'], errors='coerce')

df_from_csv['WO_normalized'] = (df_from_csv['WO [x1000]'] - df_from_csv['WO [x1000]'].min()) / (df_from_csv['WO [x1000]'].max() - df_from_csv['WO [x1000]'].min())
df_from_csv['Beer_normalized'] = (df_from_csv['NL Beer consumption [x1000 hectoliter]'] - df_from_csv['NL Beer consumption [x1000 hectoliter]'].min()) / (df_from_csv['NL Beer consumption [x1000 hectoliter]'].max() - df_from_csv['NL Beer consumption [x1000 hectoliter]'].min())

plt.figure(dpi=300)
plt.plot(df_from_csv["Year"], df_from_csv["WO_normalized"], label="WO [x1000] (Normalized)", color="blue", marker="o")
plt.plot(df_from_csv["Year"], df_from_csv["Beer_normalized"], label="NL Beer consumption [x1000 hectoliter] (Normalized)", color="green", marker="s")


plt.xlabel("Year")
plt.ylabel("Values")
plt.title("WO and NL Beer Consumption Over Time (2006-2018)")
plt.legend()
plt.grid(True)


plt.tight_layout()
plt.savefig("WO_Beer_Consumption_Plot.png", format="png")
