def list_to_int( sequence ) :
    sequence_int = list( )
    for num in sequence :
        sequence_int.append( int( num ) ) 
    return sequence_int

def is_monodi( sequence , index ) :

    if sequence[ index ] == 1 :
        return True 
    
    if sequence[ index ] % 2 == 0 :
        if sequence[ index + 1 ] == sequence[ index ] / 2 :
            return is_monodi( sequence , index + 1 ) 
        else :
            return False
    else :
        if sequence[ index + 1 ] == 3 * sequence[ index ] + 1 :
            return is_monodi( sequence , index + 1 )
        else :
            return False 
 
with open( "seq.dat" , "r" ) as sequence_file :

    cnt = 0 

    for line in sequence_file :
        cnt = cnt + 1 
        sequence = line.rstrip( ).split( " " )
        sequence = list_to_int( sequence )
        
        if is_monodi( sequence , 0 ) :
            print( f"The sequence { cnt } is valid. Its length is { len( sequence )}")
        else :
            print( f"The sequence { cnt } is NOT valid.")

