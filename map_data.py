import numpy as np
import matplotlib.pyplot as plt

#data = np.loadtext("data.csv",delimiter=',',names=['x','y'])
data = np.genfromtxt('data2.csv', delimiter=',', names=['x', 'y'])

fig = plt.figure()

plt.plot(data['x'], data['y'], color='r', label='the data')

#fig = plt.figure()
x = np.arange(1,150,5)
y = -1.0284880932 *np.log (x) + 5.429368820

plt.plot(x,y)

plt.show()



