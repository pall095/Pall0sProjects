
l1 = [ 1 , 4 , 9 , 16  ]
l2 = [ 9 , 7 , 4 , 9 , 11 ]
out = [ ]

r = min( len( l1 ) , len( l2 ) ) 

for i in range ( r ) :
    out.append( l1[ i ] )
    out.append( l2[ i ] )

if len( l2 ) > len( l1 ) :

    for j in range( i + 1 , len( l2 )  ) :
        out.append( l2[ j ] ) 

else :
    for j in range( i + 1 , len( l1 )  ) :
        out.append( l1[ j ] )

print( out )


