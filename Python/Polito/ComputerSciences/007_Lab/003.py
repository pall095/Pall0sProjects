

def zeros(  rows , cols ) :  
    table = [ ]
    row = [ 0 ] * cols 
    for i in range( rows ) :
        table.append( row ) 
    return table 

def ones( table , rows , cols ) :
    for i in range( rows ) :
        for j in range( cols ) :
            table[ i ][ j ] = 1
    return table 


def alternate( table , rows , cols ) :
    bouncer = False 
    for i in range( rows ) :
        for j in range( cols ) :
            if bouncer :
                table[ i ][ j ] = 1 
            else:
                table[ i ][ j ] = 0
            bouncer = not( bouncer )
    return table

def print_table( table , rows , cols ) :
    for i in range( rows ) :
        for j in range( cols ) :
            print( f"{ table[ i ][ j ]} - " , end="")
        print( "\n" , end = "" )
    print( "---" )




m = int( input( "Insert the number of rows: " ) ) 
n = int( input( "Insert the number of columns: " ) )

table = zeros( m , n ) 
print_table( table , m , n )
table = ones( table , m , n ) 
print_table( table , m , n  )
table = alternate( table , m , n )
print_table( table , m , n )  



