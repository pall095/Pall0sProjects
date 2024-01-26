import random as rd
import copy
from sortingMethods import mergeSort, quickSort, selectionSort, heapSort, insertionSort, selectionSort
from Sorter import Sorter
import time

import matplotlib.pyplot as plt


if __name__ == "__main__":
    
    
    low = 1
    high = 10000
    step = 10
    
    arr = rd.sample( range( 0 ,  10 * high ) , high ) 
    
    sorter_list = [  Sorter( arr , insertionSort ) ,  Sorter( arr , heapSort ) ]
    

    
    for i in range( low , high , step ):
        
        arr = rd.sample( range( 0 , 10* high ) ,  i )

        for j in range( len( sorter_list ) ):
            
            sorter_list[ j ].original_array = copy.deepcopy( arr )
            sorter_list[ j ].sort( ) 
        
        
     

    for i in range( len( sorter_list ) ) :
        plt.plot( range( low , high , step ) , sorter_list[ i ].timeArray , label = sorter_list[ i ] .method.__name__ )
        
        
    plt.legend( )
    plt.show( )    
    
    