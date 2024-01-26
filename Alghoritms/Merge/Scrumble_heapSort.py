import random as rd 

def exch( arr , k  , j ) :
    
    tmp = arr[ k ]
    arr[ k ] = arr[ j ]
    arr[ j ] = tmp
    
    

def swim( arr , k  ):
    
    father = int( k / 2 )
    
    while k > 1 and arr[ father ] < arr[ k ] :
        exch( arr , k , father )
        k = father
        father = int( k / 2 )


def sink( arr , k , N ):
    
    while 2*k <= N :
        
        j = 2 * k 
        
        if( j < N and arr[ j ] < arr[ j + 1 ] ) : j+= 1 
        if( arr[ k ] > arr[ j ] ) : break 
    
        exch( arr , k , j )
        k = j
        

    
    
def heapSort( arr ) :
    
    N = len( arr ) - 1
    i = int( N / 2 )
    
    while i >= 1 : 
       
        print( i )
        sink( arr , i , N )
        i = i - 1
        
    while( N > 1 ):
       

        exch( arr , 1 , N )
        N = N - 1 
        sink( arr , 1 , N )
   
    return arr
       
               



if __name__ == "__main__" :
    
    low = 1
    high = 20
    step = 100
    
    # Putting a zero in front to make the array "start from one". 
    arr = rd.sample( range( 0 ,  10 * high  ) , high  ) 
    arr.insert( 0 , 0 )
    #arr = [ 0 , 1 , 110 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
    
    
    #print( swim( arr , 9 ) )
    #print( sink( arr , 1 , len( arr ) ) )
    print( arr )
    print( heapSort( arr ) )
    
    