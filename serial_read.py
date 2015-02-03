import serial
import numpy as np
from scatter3D import Plot3D

# Sets up the serial input
s = serial.Serial('/dev/ttyACM0',9600,timeout=5)

value = []
for x in xrange(1,1000):
    d = int(s.readline()) # Sets the un-calibrated distanc
    #print d
    #distance = -1.0284880932 *np.log (d) + 5.429368820
    #distance = -271.0349430875 * np.log(d) + 1294.45055666669
    distance = np.exp( ( d - 1294.45056) / (-271.03494))
    value.append(distance)
    print distance,
    print "cm"

Plot3D( [value,value,value])

def ReadSerial( points ):
    s = int(serial.Serial('/dev/ttyACM0',9600,timeout=5))
    for x in xrange(points):
        d = s.readline()
        
    return [ x, y, z ]

    


