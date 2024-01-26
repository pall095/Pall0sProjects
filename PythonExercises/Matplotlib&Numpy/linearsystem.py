import matplotlib.pyplot as plt
import numpy as np


time_array = np.empty( [1 , 1 ] )
dt = 0.1

xt_array = np.empty( [ 2 , 1 ] )
x0 = np.array( [ [ 10 ] ,  [10 ] ] )

R = 1; 
L = 1;
C = 1;
G1 = 0.8;
G2 = 0.05


A = np.array( [ [ -R/L , 1/L] , [ -1/C , G1/C ] ] )


for i in range( 1000 ):
    
    if i == 0 :
        xt = x0
        
    time_array = np.append( time_array , i * dt )
    xt_array = np.append( xt_array , xt , axis =  0 )
    xdot = np.dot( A , xt )
    
    xt = xdot*dt + xt
    
print( xt_array.shape )
#plt.plot( time_array, xt_array[ 1 , : ] )
#plt.show( )