

class GameManager :
    
    def __init__( self , playerList ) :
        
        self.__playerList = playerList
        
       
    # Plays all the player given in the list against each other based on the given parameters.
    # It basically iterates throw the player list, takes the i-esim player and the opponent is always the next one (so to avoid playing twice against the same)
    # player.    
    def playTournament( self , start, step , stop , suppressOutput : bool = False ) :
            
        for i in range( len( self.__playerList ) ) :
            
            p1 = self.__playerList[ i ]
            
            for j in range( i + 1  , len( self.__playerList ) ):
                
                p2 = self.__playerList[ j ]
                
                for num in range( start, stop +  1 , step ) :
                    
                    for k in range( num ):
                        
                        self.updateScore( p1 , p2 )
                        
                        if not( suppressOutput ):
                            print( "Playing: " + p1.name + " vs." + p2.name )
                            print( "Playing game: " + str( k + 1 ) + " of " + str( num ) )
                   
    def printScore( self ) :
        
        for p in self.__playerList :
            
            print( "Player Name: " + p.name )
            print( "Player's Stragegy: " + p.method.__name__ )
            print( "Player Score: " + str( p.score ) )
            
    def printScoreboard( self ):
        
        sortedList = sorted( self.__playerList , key = lambda p: p.score  , reverse = True )
        i = 1 
        
        for p in sortedList :
            
            print( "POSITION: " + str( i )  )
            print( "\tPlayer: " + p.name )
            print( "\tStrategy: " + p.method.__name__ )
            print( "\tScore: " + str( p.score ) )
            
            i = i + 1
            
        
    # updates the score two players given the current actions. Also performs some storing of the values (stores ego action, opponent action, append score and update the action)    
    def updateScore( self , p1 , p2 ) :
        
        
        # check if the actions are equals.
        if p1.currentAction == p2.currentAction :
            
            # if they are true (it only checks one since they are already equal), gives three points to both.
            if p1.currentAction: 
                
                
                p1.score = p1.score + 3
                p2.score = p2.score + 3
                
            # if they are both false, gives one point to both.
            if not( p1.currentAction ) :
                
                p1.score = p1.score + 1 
                p2.score = p2.score + 1
                
        # if they are different, it gives 5 point to the one that is not collaborating.
        elif p1.currentAction and not( p2.currentAction ):
            
            p2.score = p2.score + 5 
            
        elif p2.currentAction and not( p1.currentAction ):
            
            p1.score = p1.score + 5
            
        p1.storeEgoAction( )
        p2.storeEgoAction( )
        p1.storeOpponentAction( p2.currentAction )
        p2.storeOpponentAction( p1.currentAction )
        p1.appendScore( )
        p2.appendScore( )
        p1.updateAction(  )
        p2.updateAction(  )