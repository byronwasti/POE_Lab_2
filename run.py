from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
import serial
from time import sleep

Time_Plot = False

def Coord_Transform_Single ( data):
    d = data[0]
    theta = data[1]
    phi = data[2]

    #d = np.exp( ( d - 1294.45056) / (-271.03494))
    d = np.exp( ( d - 1416.4651589499) / ( -301.2902022911))
    if d > 60: return 0

    z = ( d * np.cos( theta ) )
    x = ( d * np.sin( theta ) * np.cos ( phi ) )
    y = -( d * np.sin( theta ) * np.sin ( phi ) )

    return x, y, z

def Coord_Transform ( d, theta, phi):
    x = []
    y = []
    z = []

    for i in range(len(phi)):
        d[i] = np.exp( ( d[i] - 1294.45056) / (-271.03494))
        if d[i] > 60: continue

        z.append( d[i] * np.cos( theta[i] ) )
        x.append( d[i] * np.sin( theta[i] ) * np.cos ( phi[i] ) )
        y.append( d[i] * np.sin( theta[i] ) * np.sin ( phi[i] ) )

    return x, y, z

def Plot3D(x, y, z):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.scatter(x, y, z, c='r', marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

def Parse_Data ( data ):

    # Takes in string of data
    data = data.split(',')
    
    # Distance
    d = int(data[0])

    # Theta
    t = np.radians(int(data[1]))

    # Phi
    p = np.radians(int(data[2].strip('\n')))
    
    return d, t, p

def main():

    # Array that will store all of the data
    data = []
    DATA_EXPORT = []
    
    # Array that will store temporary data for 
    # plotting in time
    x = []
    y = []
    z = []

    if Time_Plot:

        # Initialize plotting functions
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.disable_mouse_rotation()
        plt.ylim(-150,150)
        plt.xlim(-150,150)
        ax.set_zlim(-150,150)

    # Setting up the initialization for the Arduino
    raw_input("Is the 3D Scanner plugged in?")
    s = serial.Serial('/dev/ttyACM0',9600,timeout=50)
    print "Getting connection..."
    sleep(2)
    s.readline()
    raw_input('Start?')

    # Killing off any 'a's left
    s.readline()

    print "Beginning data collection"
    # After this point the Arduino will start scanning and sending back data
    while True:
        
        # Set up pinging between the two devices in order to not lose data
        s.write('a')
        tmp =  s.readline()

        # TEMPORARY CODE
        #print tmp

        # Sets up ending the loop when the scan is finished
        if "STOP" in tmp: break
    
        # Start storing the values taken in
        data.append(tmp)
        DATA_EXPORT.append(tmp)

        # Plotting over time
        if Time_Plot:
            tmpx, tmpy, tmpz = Coord_Transform_Single( Parse_Data( tmp))

            x.append(tmpx)
            y.append(tmpy)
            z.append(tmpz)

            if len(x) % 20 == 0:
                ax.scatter(y,x,z,c='r',marker='.',depthshade=False)
                x = []
                y = []
                z = []
                plt.draw()
                pause(0.01)

    print "Ended data collection"
    if Time_Plot: plt.close()
    f = open('OUTPUT.txt','w')
    for i in DATA_EXPORT:
        f.write(i)

    x = []
    y = []
    z = []
    for i in data:
        try:
            tmpx, tmpy, tmpz = Coord_Transform_Single( Parse_Data( i ) )
            x.append(tmpx)
            y.append(tmpy)
            z.append(tmpz) 
        except: continue
    Plot3D(z,y,x)
    
main()
