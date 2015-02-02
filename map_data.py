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

x2 = [ 10, 20, 30, 40, 50, 60 ]
y2 = [ 521, 496, 380, 300, 245, 200 ]

ytmp = np.divide(y2, 200.0)
y2 = ytmp

plt.plot(x2, y2)

plt.show()



