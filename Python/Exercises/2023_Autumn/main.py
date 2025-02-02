
def update_most_efficient( most_efficient , efficiency , player , team ) :

    if most_efficient == [] :
        most_efficient.append( [ player , team , efficiency ] )

    for i in range( len( most_efficient ) ) :

        if efficiency > most_efficient[ i ][ 2 ] :
            most_efficient.insert( i , [ player , team , efficiency ] ) 
            break

    return most_efficient



position_query = [ "MF" , "FW" ]
most_efficient_forward = list( )
most_efficient_middle = list( )

with open( "player_stats.csv" , "r" , encoding = "utf-8") as player_file :

    player_file.readline( )
    for line in player_file :
        line = line.rstrip( )
        player , position , team , birth_year , minutes , goals , assists , offsides , crosses , interceptions , tackles_won , pens_conceded , balls_recoveries , aerial_won , aerial_lost = line.split( "," ) 
             
        if position in position_query :

            if position == "FW" :
                try :
                    efficiency = ( int( goals ) / int( minutes ) ) + ( int( goals ) / int( minutes ) ) - ( int( offsides )  / int( minutes ) ) 
                    most_efficient_forward = update_most_efficient( most_efficient_forward , efficiency , player , team )
                except ZeroDivisionError :
                    continue 
            elif position == "MF" :
                try :
                    efficiency = int( interceptions ) + int( balls_recoveries ) + ( ( int( assists )  / int( crosses ) ) / int( minutes ) )
                    most_efficient_middle = update_most_efficient( most_efficient_middle , efficiency , player , team )
                except ZeroDivisionError :
                    continue
                    

print( most_efficient_forward[ 0 : 3 ] )
print( most_efficient_middle[ 0 : 3 ] )


        
