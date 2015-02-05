import numpy as np

def Coord_Transform ( d, theta, phi):
    x = []
    y = []
    z = []
    for i in range(len(d)):
        d[i] = np.exp( ( d[i] - 1294.45056) / (-271.03494))
        z.append( d[i] * np.cos( phi[i] ) )
        x.append( d[i] * np.sin( theta[i] ) * np.cos ( phi[i] ) )
        y.append( d[i] * np.sin( theta[i] ) * np.sin ( phi[i] ) )

    return x, y, z


