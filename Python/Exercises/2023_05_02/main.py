
def word_difference( w1 , w2 ) :

    difference = 0 

    for i in range( len( w1 ) ) :

        if( w1[ i ] != w2[ i ] ) :
            difference = difference + 1 

    return difference 
        

def find_similar( word , word_db ) :

    word_lower = word.lower( )
    similar_list = list( )
    for w in word_db :

        if( len( w ) != len( word_lower ) ) :
            continue 
        else :
            if word_difference( w , word_lower ) == 1  :
                similar_list.append( w ) 

    return similar_list

db_list = list( )

with open( "parole_italiane.txt" , "r" ) as word_db :

    for line in word_db :
        line = line.rstrip( )
        db_list.append( line )


word = input( "Insert the word file reference: " ) 

with open( word , "r" ) as word_file :

    for line in word_file :
        w = line.rstrip( ) 
        similar = find_similar( w , db_list)

        if( len( similar ) != 0 ) :
            print( f"Name { w } :" )
            for word in similar :
                print( word ) 
        else :
            print( f"WARNING no similar word were found for { w }")
    



