
from matplotlib import pyplot as plt
from matplotlib import style
from numpy import genfromtxt

data = genfromtxt('Data/unemployment.csv',delimiter=' ')

plt.plot(data)
plt.show
