

PARK_LENGTH = 11
parking_spots = [ False ] * PARK_LENGTH 

def print_spots( parking_spots , PARK_LENGTH ) :

    for i in range( PARK_LENGTH ) :

        if parking_spots[ i ] :
            print( "x" , end = "" )
        else:
            print( "_" , end = "" ) 

def find_spot( parking_spots , PARK_LENGTH ) :

    longets_vacant_length = 0 
    longets_vacant_start = 0 
    current_vacant_length = -1
    current_vacant_start = -1

    if True not in parking_spots :
        return PARK_LENGTH//2

    for i in range( PARK_LENGTH ) :
        if parking_spots[ i ] == True or i == PARK_LENGTH - 1 :
            if current_vacant_length > longets_vacant_length :
                longets_vacant_length = current_vacant_length 
                longets_vacant_start = current_vacant_start
            current_vacant_start = -1 
            current_vacant_length = -1
        else :
            if current_vacant_start == -1 :
                current_vacant_start = i 
                current_vacant_length = 1 
            else :
                current_vacant_length += 1 
            



    print( f"Longest sequence start: { longets_vacant_start } - Longest sequence length :{longets_vacant_length } " )
    return longets_vacant_start + longets_vacant_length//2


while False in parking_spots :

    spot = find_spot( parking_spots , PARK_LENGTH ) 
    parking_spots[ spot ] = True 
    print_spots( parking_spots , PARK_LENGTH )
    input( )








