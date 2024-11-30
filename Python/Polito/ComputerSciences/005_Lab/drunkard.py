import random as rd 


def move( pos , direction ) :

    if direction == 1 : # North
        return [ pos[ 0 ] + 1  , pos[ 1 ] ]
    elif direction == 2 : #South
        return[ pos[ 0 ] -  1 , pos[ 1 ] ] 
    elif direction == 3 : #east
        return[ pos[ 0 ] , pos[ 1 ] + 1 ] 
    elif direction == 4 : #west
        return[ pos[ 0] , pos[ 1 ] -  1 ] 

pos = [ 0 , 0 ] 
for i in range( 100 ) :
    pos = move( pos , rd.randint( 1 , 4 ) )
    print( pos ) 





