import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('istherecorrelation.csv',sep = ';')

time = data.iloc[:,0]
wo = [float(i.replace(',','.')) for i in data.iloc[:,1]]
norm_wo = [i/wo[0] for i in wo]
norm_alcohol = data.iloc[:,2]/data.iloc[0,2]

plt.plot(time,norm_wo,color = 'red',label = 'wo students')
plt.plot(time,norm_alcohol, label = 'alcohol consumption')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Proportion to 2006')
plt.title('Increase in WO students and alcohol consumption in the \n Netherlands (1 represents 2006 levels)')
plt.savefig('Plot_alcohol_nl.png',dpi = 300)

np.corrcoef(wo,data.iloc[:,2])
np.corrcoef