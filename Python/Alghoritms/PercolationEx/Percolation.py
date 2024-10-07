import numpy as np

class Percolation:
    
    def __init__( self , sz ):
        
        self.grid = np.zeros( (sz , sz ) )
        self.id = np.arange(start = 0, stop = sz*sz )
        self.sizes = np.zeros( self.id.shape )
        self.sz = sz
    
    def countOpen( self ):
        
        counter = 0 
        
        for i in range( self.sz ):
            for j in range( self.sz ):
                
                if( self.isOpen( i , j ) ):
                    counter += 1 
                    
        return counter
    
    def initializeVirtualNodes( self ):
        
        self.id[ 0 : self.sz ] = np.zeros( self.sz )
        self.id[ len( self.id ) - self.sz - 1 : len( self.id ) - 1 ] = ( self.sz**2 - 1 ) * np.ones( self.sz )

    def rowcol2index( self , r , c ):
        
        return r*self.sz + c
    
    def isConnectable( self , r1 , c1 , r_master , c_master ):
        
        # Checking if the node to connect is further away than a row.
        if r1 > r_master + 1 or r1 < r_master - 1 :
            return False
        
        # Checking if the node to connect is further away than column.
        if c1 > c_master + 1 or r1 < r_master - 1 :
            return False
        
        # Checking sud-est diagonal.
        if r1 == r_master + 1 and c1 == c_master + 1 :
            return False
        
        # Checking sud-ovest diagonal.
        if r1 == r_master + 1 and c1 == c_master - 1 :
            return False
        
        # Checking nord-est diagonal
        if r1 == r_master - 1 and c1 == c_master + 1 :
            return False
        
        # Checking nord-ovest diagonal
        if r1 == r_master - 1 and c1 == c_master - 1 :
            return 
        
        return True
    
    def isOpen( self , r , c ):
        

        if r > 0 :
            if not( self.isConnected( r , c , r - 1 , c ) ) :
                return False
        
        if c > 0 :
            if not( self.isConnected( r , c , r , c - 1 ) ) :
                return False
            
        if r < self.sz - 1 :
            if not( self.isConnected( r , c , r + 1 , c ) ):
                return False
        
        if c < self.sz - 1 :
            if not( self.isConnected( r , c , r  , c + 1 ) ) :
                return False
            
        return True
        

    def open( self , r , c ):
             
        if r > 0 :
            self.connect( r - 1 , c , r , c )
            
        if c > 0 :
            self.connect( r , c - 1 , r , c )
            
        if r < self.sz - 1:
            self.connect( r + 1 , c , r , c )
            
        if c < self.sz - 1:
            self.connect( r , c + 1 , r , c )
            
        self.grid[ r ][ c ] = 1 
            
    def isFull( self , r , c ):
        
        for i in range( self.sz ):
            
            if( self.isConnected( 0 , i , r , c) ):
                
                return True
            
        return False
    
    def percolates( self ):
        
        for i in range( self.sz ):
            
            if( self.isFull( self.sz - 1 ,  i ) ):
                return True
            
        return False
                
    def root( self , r , c ):
        
        index = self.rowcol2index( r , c )
        
        while( self.id[ index ] != index ):
            
            index = self.id[ index ]
            
        return index
    
    def isConnected( self , r1 , c1 , r2 , c2 ):
        
        return self.root( r1 , c1 ) == self.root( r2 , c2 )
    
    
    def connect( self , r1 , c1 , r2 , c2 ):
        
        if( self.isConnectable( r1 , c1 , r2 , c2 ) ) :
            
            indexP = self.rowcol2index( r1 , c1 )
            indexQ = self.rowcol2index( r2 , c2 )
            rootP = self.root( r1 , c1 )
            rootQ = self.root( r2 , c2  )
            self.id[ rootP ] = rootQ
            
        else:
            
            print( "Nodes are incompatible! They cannot be connected")
    
    
        
        
                
        
        