import matplotlib.pyplot as plt

with open("istherecorrelation.csv") as f:
data = f.read()

data = data.split('\n')

x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]

plt.figure()
plt.plot(x,y)
