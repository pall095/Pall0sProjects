import random as rd
import copy

def swap( arr , i , j ):
    
    temp = arr[ i ]
    arr[ i ] = arr[ j ]
    arr[ j ] = temp 
    
    
def partition( arr , lo , hi ) :
    
    partitioning_element = arr[ 0 ] 
    
    i = lo + 1
    j = hi 
    
    while True :
        
        while arr[ i ] < arr[ lo ] :
            i = i + 1
            if i == hi : break
            
        while arr[ j ] > arr[ lo ] :
            j = j - 1
            if j == lo : break
        
        
        if i >= j : break
    
        swap( arr , i , j )
        
    swap(arr , lo , j )
    return j 

def quickSort( arr , lo , hi ):
    
    if hi <= lo : return
    
    j = partition( arr , lo , hi )
    quickSort( arr, lo , j - 1 )
    quickSort( arr , j + 1 , hi )
    return arr

    
    

def selectionSort( arr : list ):
    
    for i in range( len( arr ) ):
        
        minimum_index = i 
        
        for j in range( i + 1 , len( arr ) ):
            
            if( arr[ j ] < arr[ minimum_index ] ) :
                
                minimum_index = j
                
        swap( arr , i  , minimum_index )
        
    return arr


def insertionSort( arr : list ):
    
    for i in range( len( arr ) ):
        
        for j in range( i , 0 ):
            
            if( arr[ i ] < arr[ j ] ):
                
                swap( arr , i  , j )
                
            else: break
           
    return arr 


def merge( arr , lo , mid , hi ) :
    
    i = lo 
    j = mid + 1
    
    aux= copy.deepcopy( arr )
    
    for k in range( lo , hi + 1 ):
        
        if( i > mid ):
            arr[ k ] = aux[ j ]
            j = j + 1
            
        elif( j > hi ):
            
            arr[ k ] = aux[ i ]
            i = i + 1
            
        elif aux[ i ] >= aux[ j ] :
            
            arr[ k ] = aux[ j ]
            j = j + 1
        else:
            arr[ k ] = aux[ i ]
            i = i + 1
            
    return arr
        

def mergeSort( arr : list ,  lo , hi ):
    
    if( lo >= hi ) : return
    
    mid = int( lo + ( hi - lo ) / 2 )
    mergeSort( arr ,  lo , mid )
    mergeSort( arr ,  mid + 1 , hi )
    merge( arr ,  lo , mid , hi )
    return arr




def swim( arr , k  ):
    
    father = int( k / 2 )
    
    while k > 1 and arr[ father ] < arr[ k ] :
        swap( arr , k , father )
        k = father
        father = int( k / 2 )
        


def sink( arr , k , N ):
    
    while 2*k <= N :
        
        j = 2 * k 
        
        if( j < N and arr[ j ] < arr[ j + 1 ] ) : j+= 1 
        if( arr[ k ] > arr[ j ] ) : break 
    
        swap( arr , k , j )
        k = j
        

    
    
def heapSort( arr ) :
    
    N = len( arr ) - 1
    i = int( N / 2 )
    
    while i >= 1 : 
       
        sink( arr , i , N )
        i = i - 1
        
    while( N > 1 ):
       

        swap( arr , 1 , N )
        N = N - 1 
        sink( arr , 1 , N )
        
    return arr
   
       
    
    