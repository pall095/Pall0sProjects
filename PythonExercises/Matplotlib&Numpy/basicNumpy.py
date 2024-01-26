import numpy as np
import matplotlib.pyplot as plt

PI = 3.14

x = np.arange( 0 , 2*PI , 0.1 )
y1 = np.sin( x )
y2 = np.cos( x )


plt.plot( x , y1 ) 
plt.plot( x , y2 )
plt.show( )



