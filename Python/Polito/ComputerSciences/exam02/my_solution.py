
word_db_list = [ ] 
names = [ ]


def count_difference( w1 , w2 ) :

    diff_counter = 0 

    for i in range( len( w1 ) ):
        if w1[ i ] != w2[ i ] :
            diff_counter = diff_counter + 1 

    return diff_counter 


def find_candidates( name , word_db_list , allowed_difference = 1 ) :

    valid_candidates = [ ] 
    for candidate in word_db_list :
        if len( candidate ) != len( name ) :
            continue       
        diff_count = count_difference( name , candidate )
        if diff_count <= allowed_difference :
            valid_candidates.append( candidate )
    return valid_candidates



with open( "parole_italiane.txt" , "r" ) as word_db_file :

    for line in word_db_file :
        word_db_list.append( line.rstrip() ) 

word_db_file.close()

name_file = input( "Please, introduce the name of the file with the names: \n" )
with open( name_file , "r" ) as file :
    for line in file :
        names.append( line.rstrip( ).lower( ) )
file.close( )

for name in names :
    valid_candidates = find_candidates( name.lower( ) , word_db_list )
    if len( valid_candidates ) > 0 :
        print( f"Valid subsistutes for { name } are :" )

        for candidate in valid_candidates :
            print( candidate )
    else:
        print( f"No valida candidates for { name }")


    


        