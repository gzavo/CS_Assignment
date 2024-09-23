import numpy as np
import matplotlib.pyplot as plt
import polars as pl



data = pl.read_csv("istherecorrelation.csv", separator=";", decimal_comma=True)
# print()
# print(year := data.get_column("Year").to_numpy())
# print(wo := data.get_column("WO [x1000]").to_numpy())
# fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()
# ax1.plot(data["Year"], data["WO [x1000]"], "-b", label = "Students")
# ax2.plot(data["Year"], data["NL Beer consumption [x1000 hectoliter]"], "-r", label="Beer")
# ax1.set_xlabel("Year")
# ax1.set_ylabel("WO Students [x1000]")
# ax2.set_ylabel("NL Beer consumption [x1000 hectoliter]")
# plt.title("Correlation between amount of University students and beer consumption")
# ax1.legend()
# plt.show()
percentages = (
    data.select(
        pl.col("Year"),
        (pl.col("WO [x1000]") / pl.col("WO [x1000]").first()).alias("student percentage"),
        (pl.col("NL Beer consumption [x1000 hectoliter]") / pl.col("NL Beer consumption [x1000 hectoliter]").first()).alias("beer percentage"),
    )
)
plt.plot(percentages["Year"], percentages["student percentage"], "-b", label="Students")
plt.plot(percentages["Year"], percentages["beer percentage"], "-r", label="Beer")
plt.xlabel("Year")
plt.ylabel("% increase")
plt.title("Correlation between amount of University students and beer consumption")
plt.legend()
plt.savefig("correlation.png", dpi=300)
