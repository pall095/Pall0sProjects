alice_box = list( )

MAX_BOX = 42
GIVE = "Bob gives"
TAKE = "Carl takes"
SPLIT = "a "
time = 0 


with open( "actions-fail_bob.txt" , "r" ) as action_file :

    for line in action_file :

        line = line.rstrip( )
        action , item = line.split( sep = SPLIT )
        print( f"{ time } - { line } -- { len( alice_box )}" , end = " -- " )

        if GIVE in action :
            if item in alice_box :
                print( f"{ item } already in Boxes" )
            elif len( alice_box ) >= MAX_BOX :
                print( f"{ item } cannot be stored because alice boxes are full" )
            else :
                print( f"{ item } added to Alice Box" )
                alice_box.append( item ) 
        elif TAKE in action :

            try :
                index = alice_box.index( item )
            except ValueError :
                index = -1 

            if index == -1 :
                print( f"{ item } cannot be retreived " )
            else :
                print( f"{ item } taken from the boxes" )
                alice_box.pop( index )
        
        time = time + 1 
        input( )
