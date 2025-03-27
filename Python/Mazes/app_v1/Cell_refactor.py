


class Cell:
    
    def __init__( self , row , col , state , depth ) :
    
        self.row = row 
        self.col = col 
        self.state = state
        self.depth = 0 
        self.cost = 0 
        self.path = [ ]
        
    
    @property
    def state( self ) :
        return self.__state 
    @state.setter
    def state( self , newState ) :
        self.__state = newState
        
    @property
    def depth( self ) :
        return self.__depth
    @depth.setter
    def depth( self , newDepth ) :
        self.__depth = newDepth
        
    @property
    def cost( self ) :
        return self.__cost 
    @cost.setter
    def cost( self , newCost ) :
        self.__cost = newCost 
        
    
    

                