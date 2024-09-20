import pandas as pd
import matplotlib.pyplot as plt


# Simulating the creation of a CSV file to read from
csv_file_path = "./istherecorrelation.csv"

# Reading the data from the CSV file
df_from_csv = pd.read_csv(csv_file_path, sep=';', decimal=',')

# Plotting the data again, read from the CSV
plt.figure(dpi=300)
plt.plot(df_from_csv["Year"], df_from_csv["WO [x1000]"], label="WO [x1000]", color="blue", marker="o")
plt.plot(df_from_csv["Year"], df_from_csv["NL Beer consumption [x1000 hectoliter]"], label="NL Beer consumption [x1000 hectoliter]", color="green", marker="s")

# Adding labels and title
plt.xlabel("Year")
plt.ylabel("Values")
plt.title("WO and NL Beer Consumption Over Time (2006-2018)")
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.savefig("WO_Beer_Consumption_Plot.png", format="png")
