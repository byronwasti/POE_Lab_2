import serial
import numpy as np


# Sets up the serial input
s = serial.Serial('/dev/ttyACM0',9600,timeout=5)

for x in xrange(1,100000):
    d = int(s.readline()) # Sets the un-calibrated distanc
    #print d
    distance = -1.0284880932 *np.log (d) + 5.429368820
    print distance



    


