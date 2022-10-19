import csv
import matplotlib.pyplot as plt

exampleFile = open('istherecorrelation.csv')  
exampleReader = csv.reader(exampleFile) 
exampleData = list(exampleReader) 
length_row = len(exampleData)  
length_c = len(exampleData[0])  

x = list()
y = list()

for i in range(1, length_row):  
    x.append(exampleData[i][0])  
    y.append(exampleData[i][1])  

plt.plot(x, y) 
plt.show()  
plt.xlabel('time (years)')
plt.ylabel('WO [x1000]')
plt.title('Beer consumption [x1000 hectoliter]')
