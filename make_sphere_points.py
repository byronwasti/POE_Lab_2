d = 10;
f = open('points.txt','w')
for i in range(0,361,10):
    for j in range(0,361,10):
        f.write( str(d)+','+str(i)+','+str(j)+'\n')

