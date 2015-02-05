from scatter3D import Plot3D
from serial_read import ReadSerial
from fix_data import Coord_Transform


points = 500
data = ReadSerial( points )
#data = [ "10,0,0","10,180,90","50,0,0"]

d = []
t = []
p = []
for i in range(len(data)):
    print data[i]
    data[i] = data[i].split(',')
    d.append(int(data[i][0]))
    t.append(int(data[i][1]))
    p.append(int(data[i][2]))

x, y, z = Coord_Transform( d, t, p )

Plot3D(x, y, z)
