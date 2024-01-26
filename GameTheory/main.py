from Player import Player
from Strategies import swapOppnent, alwaysNice, friedman, titForTat, rand
import numpy as np
import matplotlib.pyplot as plt
from GameManager import GameManager




if __name__ == "__main__" :
    
    #Game parameters
    start = 1
    step = 1
    stop = 50
    numGames = np.arange( start , stop , step  )


    p1 = Player( "One" , True , titForTat )
    p2 = Player( "Two" , True , swapOppnent )
    p3 = Player( "Three" , True , rand )
    p4 = Player( "Four" , True , friedman )
    p5 = Player( "Five" , True , alwaysNice )
    
    
    manager = GameManager( Player.playerList )
    manager.playTournament( start , step , stop , suppressOutput = True ) 
    manager.printScoreboard( )
    
    
    
    for player in Player.playerList :
        
        plt.plot( range( len( player.scoreList) ) , np.array( player.scoreList ) , label = player.method.__name__ )
    

    plt.legend( )
    plt.show( ) 
 
         
        
    #printResult( p1 , p2 )    
    
    
    
    
    
        
    
    