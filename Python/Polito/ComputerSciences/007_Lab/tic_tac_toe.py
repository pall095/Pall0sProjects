
def display_grid( grid , ROWS , COLS ) :

    for i in range( ROWS ) :
        for j in range( ROWS  ) :
            print( f"{grid[ i ][ j ]} " , end = "") 

        print( "\n" , end = "" ) 

def check_win( grid , ROWS , COLS , key ) :

    for i in range( ROWS ) :
        if grid[ i ][ : ] == [ key ] * COLS :
            return True


    for j in range( COLS ) :
        col = [ ]
        for i in range( ROWS  ):
            col.append( grid[ i ][ j ] )

        if col == [ key ] * ROWS :
            return True 
        
    diag_1 = [ ] 
    diag_2 = [ ]
    for i in range( ROWS ) :
        diag_1.append( grid[ i ][ i ] )
        diag_2.append( grid[ i ][ ROWS - 1 - i ] )

    if diag_1 == [ key ] * ROWS or diag_2 == [ key ] * ROWS :
        return True
     
    return False


ROWS = 3 
COLS = 3
P1_KEY = "o"
P2_KEY = "x"
grid = [ ]

for i in range( ROWS ):
    row = [ "-" ] * COLS
    grid.append( row ) 


winner = False 
p1_turn = True 

while not winner :
    
    if p1_turn :
        r , c  = input( "Player 1, input where to put the o, use row:col : " ).split( ":" ) 

        grid[ int( r ) - 1  ][ int( c ) - 1 ] = P1_KEY
        if check_win( grid , ROWS , COLS , P1_KEY ) :
            print( "P1 is the winner!\n" )
            winner = True 
        else:
            p1_turn = not p1_turn
        
    else :
        r , c  = input( "Player 2, input where to put the x, use row:col : " ).split( ":" ) 
        grid[ int( r ) - 1  ][ int( c ) - 1 ] = P2_KEY
        
        if check_win( grid , ROWS , COLS , P2_KEY ) :
            print( "P2 is the winner!\n" )
            winner = True 
        else:
            p1_turn = not p1_turn  

    display_grid( grid , ROWS , COLS ) 


