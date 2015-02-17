from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
import serial
from time import sleep

test_plots = True

def Coord_Transform ( d, theta, phi):
    x = []
    y = []
    z = []
    xb = []
    yb = []
    zb = []

    for i in range(len(phi)):
        d[i] = np.exp( ( d[i] - 1294.45056) / (-271.03494))

        #if d[i] > 35: continue # and d[i] < 50: continue
        '''
        if d[i] >= 50:
            zb.append( d[i] * np.cos( theta[i] ) )
            xb.append( -d[i] * np.sin( theta[i]  ) * np.cos ( phi[i] ) )
            yb.append( d[i] * np.sin( theta[i] ) * np.sin ( phi[i] + (pi/180 * 8)) )
            continue
        '''

        z.append( d[i] * np.cos( theta[i] ) )
        x.append( -d[i] * np.sin( theta[i]  ) * np.cos ( phi[i] ) )
        y.append( d[i] * np.sin( theta[i] ) * np.sin ( phi[i] + (pi/180 * 8)) )

    return x, y, z, xb, yb, zb


def Coord_Transform_Single ( d, theta, phi):

    d = np.exp( ( d - 1294.45056) / (-271.03494))

    z = ( d * np.cos( theta ) )
    x = ( d * np.sin( theta ) * np.cos ( phi ) )
    y = ( d * np.sin( theta ) * np.sin ( phi ) )

    return x, y, z


def Plot3D(x, y, z, color, sd):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.scatter(x, y, z, c=color,marker='.',depthshade=True)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

def ReadSerial( points ):
    s = serial.Serial('/dev/ttyACM0',9600,timeout=5)
    data = []
    for x in xrange(points):
        d = s.readline()
        data.append(d)

    return data


def main():
    name = 'OUTPUT.txt'
    points = 5000
    if test_plots == True:
        data = []
        num_lines = sum(1 for line in open(name))
        f = open(name,'r')
        for i in range(num_lines):
            data.append(f.readline())
    else:
        data = ReadSerial( points )

    d = []
    t = []
    p = []
    for i in range(len(data)):
        data[i] = data[i].split(',')
        try:
            d.append(int(data[i][0]))
            t.append(np.radians(int(data[i][1])))
            p.append(np.radians(int(data[i][2].strip('\n'))))
        except:
            continue

    x, y, z, xb, yb, zb = Coord_Transform( d, t, p )
    X = []
    Y = []
    Z = []
    '''
    for i in xrange(len(x)):
        for j in xrange(len(x)):
            if x[i] == x[j] and y[i] == y[j] and z[i] == z[j]:
                break
            #print ( (x[i] - x[j])**2 + (y[i] - y[j])**2 + (z[i] - z[j])**2 )**.5
            if ( (x[i] - x[j])**2 + (y[i] - y[j])**2 + (z[i] - z[j])**2 )**.5 < 1:
                X.append(x[i])
                Y.append(y[i])
                Z.append(z[i])
                break
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.scatter(z, y, x, c='r',marker='.',depthshade=True)
    ax.scatter(zb, yb, xb, c='b',marker='.',depthshade=True)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
    '''

    Plot3D(z, y, x, 'r', 0)
    #Plot3D(zb, yb, xb, 'b', 1)
    #Plot3D(Z, Y, X, 'r', 0)

main()
