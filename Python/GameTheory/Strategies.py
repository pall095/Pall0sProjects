import random

def swapOppnent( opponentList ):
    
    return not( opponentList[ len( opponentList )  - 1 ] )


def alwaysNice( opponentList ) :
    
    return True 


# If the opponent just defects once, it will always defect.
def friedman( opponentList ) :
          
    return not( False in opponentList )

    
# Copies what the opponent has done at the last move. If follows defection with defection and cooperation with cooperation
def titForTat( opponentList ):
    
    return opponentList[ len( opponentList )  - 1 ]


def rand( opponentList ) :
    
    return bool( random.getrandbits( 1 ) )


    
    

