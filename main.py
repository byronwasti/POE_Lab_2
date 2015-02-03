from scatter3D import Plot3D
from serial_read import ReadSerial

data = [ [1,2,3],
         [3,4,5],
         [6,7,8] ]

points = 500
data = ReadSerial( points )

Plot3D(data)
