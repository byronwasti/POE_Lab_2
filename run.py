from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
import serial
from time import sleep

Time_Plot = 0

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

def main():
    # Setting up the initialization for the Arduino

    raw_input("Is the 3D Scanner plugged in?")
    s = serial.Serial('/dev/ttyACM0',9600,timeout=50)
    sleep(2)
    print "Getting connection..."
    s.readline()
    raw_input('Start?')

    # After this point the Arduino will start scanning and sending back data
    for i in range(10):
        x = str(i)
        
        # Set up pinging between the two devices in order to not lose data
        s.write(x)
        var =  s.readline()

        # Sets up ending the loop when the scan is finished
        if "STOP" in var: break
        
        print i
        print var

main()
