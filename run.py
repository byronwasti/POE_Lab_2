from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
import serial
from time import sleep

Time_Plot = False

def Coord_Transform ( d, theta, phi):
    x = []
    y = []
    z = []

    for i in range(len(phi)):
        d[i] = np.exp( ( d[i] - 1294.45056) / (-271.03494))

        z.append( d[i] * np.cos( theta[i] ) )
        x.append( d[i] * np.sin( theta[i] ) * np.cos ( phi[i] ) )
        y.append( d[i] * np.sin( theta[i] ) * np.sin ( phi[i] ) )

    return x, y, z

def Parse_Data ( data ):

    # Takes in string of data
    data = data.split(',')
    
    # Distance
    d = int(data[0])

    # Theta
    t = np.radians(int(tmp[1]))

    # Phi
    p = np.radians(int(tmp[2].strip('\n')))
    
    return d, t, p

def main():

    # Array that will store all of the data
    data = []
    
    # Array that will store temporary data for 
    # plotting in time
    tmpdata = []

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
    sleep(2)
    print "Getting connection..."
    s.readline()
    raw_input('Start?')

    # After this point the Arduino will start scanning and sending back data
    while True:
        
        # Set up pinging between the two devices in order to not lose data
        s.write('a')
        tmp =  s.readline()

        # Sets up ending the loop when the scan is finished
        if "STOP" in tmp: break
    
        # Start storing the values taken in
        data.append(tmp)
        if Time_Plot:
            tmpdata.append(tmp)
        
        
        print i
        print var

    
main()
