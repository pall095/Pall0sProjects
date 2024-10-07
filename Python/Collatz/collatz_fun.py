def collatz( n : int ):
    
    
    if( n == 1 ):
        return n

    elif( n % 2 == 0 ):
        
        return n/2 
    
    elif( n % 2 != 0 ):
        
        return 3*n + 1