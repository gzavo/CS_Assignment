import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv(r'C:\Users\kayad\OneDrive\Desktop\Master - Computational Science\Academic Skills - CLS\istherecorrelation.csv')
X = Data['Year']
Y = Data['NL Beer consumption [x1000 hectoliter]']

plt.figure(dpi=300)
plt.plot(X,Y)
plt.xlabel('Year')
plt.ylabel('NL Beer consumption [x1000 hectoliter]')
plt.title('Increase in beer consumption in the Netherlands')
