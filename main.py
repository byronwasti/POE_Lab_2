from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import serial

def Coord_Transform ( d, theta, phi):
    x = []
    y = []
    z = []
    #print len(d), len(theta), len(phi)
    for i in range(len(phi)):
        d[i] = np.exp( ( d[i] - 1294.45056) / (-271.03494))

        z.append( d[i] * np.cos( theta[i] ) )
        x.append( d[i] * np.sin( theta[i] ) * np.cos ( phi[i] ) )
        y.append( d[i] * np.sin( theta[i] ) * np.sin ( phi[i] ) )

    return x, y, z

def Plot3D(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    '''
    x =data[0]
    y =data[1]
    z =data[2]
    '''

    ax.scatter(x, y, z, c='r', marker='o')

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
    points = 500

    if test_plots == True:
        data = []
        num_lines = sum(1 for line in open('points.txt'))
        f = open("points.txt",'r')
        for i in range(num_lines):
            data.append(f.readline())
    else:
        data = ReadSerial( points )

    #print data

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
    
    #print  len(d), len(t), len(p)
    x, y, z = Coord_Transform( d, t, p )

    Plot3D(x, y, z)

main()
