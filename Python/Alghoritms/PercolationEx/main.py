from Percolation import Percolation
import random as rand
import numpy as np



if __name__ == "__main__":
    
    sz = 5
    grid = Percolation( sz )
    grid.connect( 1 , 0 , 0 , 0 )
    grid.connect( 2 , 0 , 1 , 0 )
    grid.connect( 3 , 0 , 2 , 0 )
    grid.connect( 4 , 0 , 3 , 0 )
    
    
    

    print( np.reshape( grid.id , grid.grid.shape ) )