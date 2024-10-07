

class Player:
    
    
    playerList = [ ]
    
    def __init__( self , name , initialAction : bool , method ) :
        
        self.__name = name
        self.__currentAction = initialAction 
        self.__actionList = [ ]
        self.__oppenentList = [ ]
        self.__score = 0 
        self.__method = method
        self.__scoreList = [ ]
        Player.playerList.append( self )
        
    
    def updateAction( self ) :
        
        self.__currentAction = self.__method( self.__oppenentList )
        
    
    @property
    def name( self ):
        return self.__name
    
    @property
    def scoreList( self ):
        return self.__scoreList
    @property
    def currentAction( self ):
        return self.__currentAction
    
    @property
    def actionList( self ):
        return self.__actionList
    
    @property
    def opponentList( self ):
        return self.__oppenentList
    
    @property
    def score( self ):
        return self.__score
    
    @property
    def method( self ):
        return self.__method
    
    
    @name.setter
    def name( self , newName ):
        self.__name = newName 
        
    @currentAction.setter
    def currentAction( self , newAction ):
        self.__currentAction = newAction 
        
    
    def storeEgoAction( self ):
        self.__actionList.append( self.__currentAction )
        
    
    def storeOpponentAction( self , oppentnsAction ):
        self.__oppenentList.append( oppentnsAction )
        
    def appendScore( self ):
        self.__scoreList.append( self.__score )
    
    
    @score.setter
    def score( self , newScore ):
        self.__score = newScore 
        
        
    
    
    
        
    