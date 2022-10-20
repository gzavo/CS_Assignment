import plotly.express as px
import plotly.io as pio
import pandas as pd

# Reading data
df = pd.read_csv("istherecorrelation.csv", delimiter=';')
# Creating figure
fig = px.line(df, x="Year", y="NL Beer consumption [x1000 hectoliter]", title='Beer consumption by year in the Netherlands')
# Saving figure
DPI = 300
pio.write_image(fig, "beer_graph.svg", width=6*DPI, height=3*DPI)