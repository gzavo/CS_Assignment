from matplotlib import pyplot as plt

Year = [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
WO = [205.9, 208.6, 212.7, 220.5, 233.2, 242.4, 245.4, 241.4, 250.2, 255.7, 261.2, 267.9, 280.1]
Beer = [11402, 11492, 11450, 11502, 11474, 11480, 11452, 11484, 11555, 11601, 11731, 11862, 12048]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Years')
ax1.set_ylabel('NL Beer consumption [x1000 hectoliter]', color='red')
ax1.plot(Year, Beer, color='red')
ax1.tick_params(axis='y', labelcolor='red')

ax2 = ax1.twinx()
ax2.set_ylabel('WO (x1000)', color='blue')
ax2.plot(Year, WO, color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

plt.show()
