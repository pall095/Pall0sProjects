import copy 
from sortingMethods import selectionSort, insertionSort, mergeSort, quickSort, heapSort
import time

class Sorter:
    
    
    def __init__( self , array  , method ):
        
        self.original_array = array 
        self.sorted_array = [ ]
        self.method = method 
        self.t = 0 
        self.timeArray = [ ]
        
        
        
    def sort( self ):
        
        self.t = time.time( )
        
        # For merge and quick sort, takes care of givin the two extra arguments (lo, hi )
        if self.method.__name__ == "mergeSort" or self.method.__name__ == "quickSort"  :            
            self.sorted_array = self.method( copy.deepcopy( self.original_array ) , 0 , len( self.original_array ) - 1 )
        
        # For heap sort, add a -1 element at the beginning, so to shift the first valuable index of the array to index 1.
        elif self.method.__name__ == "heapSort" :
            self.sorted_array = copy.deepcopy( self.original_array )
            self.sorted_array.insert( 0 , -1 )
            self.sorted_array = self.method( self.sorted_array )
            
        else:

            self.sorted_array = self.method( copy.deepcopy( self.original_array ) )
            
        self.t = time.time( ) - self.t 
        self.timeArray.append( self.t )
        
        