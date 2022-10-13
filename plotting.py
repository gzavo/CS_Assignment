import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('istherecorrelation.csv')
df['WO [x1000]'].plot()