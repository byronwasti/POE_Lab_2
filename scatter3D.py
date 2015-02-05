from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 

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
