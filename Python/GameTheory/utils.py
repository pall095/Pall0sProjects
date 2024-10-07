def printResult( p1 , p2 ):
    
    print( "Player 1: " )
    #print( "_Action list: " + str( p1.actionList ) )
    print( "_Strategy: " + str( p1.method.__name__ ) )
    print( "_Score: " + str( p1.score ) )
    print( "\n")
    print( "Player 2: " )
    #print( "_Action list: " + str( p2.actionList ) )
    print( "_Strategy: " + str( p2.method.__name__ ) )
    print( "_Score: " + str( p2.score ) )
    
    ans = input( "Want to show the action list?\nY --> yes\nN--> no\n" )
    
    if( ans == "y" ):
        
        print( "Player 1: " )
        print( "_Action list: " + str( p1.actionList ) )
        print( "---")
        print( "Player 2: " )
        print( "_Action list: " + str( p2.actionList ) )


