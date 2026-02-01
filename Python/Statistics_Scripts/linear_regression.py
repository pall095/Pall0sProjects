from prettytable import PrettyTable

round_precision = 2
Xi = [ 2 ,3 ,5 , 10 , 15 ]
Yi = [ 4 , 5 , 8, 9 , 13 ]

X_avg = sum( Xi ) / len( Xi )
Y_avg = sum( Yi ) / len( Yi )

Sxy = 0
Sxx = 0 
Syy = 0 

table = PrettyTable(  [ "Xi" , "Yi" , "Xi - X_avg" , "( Xi - X_avg )^2" , "Yi - Y_avg" , "( Yi - Y_avg )^2" , "( Xi - X_avg ) * ( Yi - Y_avg )" ] )
for i in range( len( Xi ) ) :

    dX_current = round( Xi[ i ] - X_avg , round_precision ) 
    dY_current = round( Yi[ i ] - Y_avg , round_precision ) 
    dX2_current = round( dX_current ** 2 , round_precision )
    dY2_current = round( dY_current ** 2 , round_precision ) 

    table.add_row( [ Xi[ i ]  ,  Yi[ i ] , dX_current , dX2_current , dY_current , dY2_current , round( dX_current * dY_current , round_precision ) ] )
    
    Sxy = Sxy + dX_current * dY_current
    Sxx = Sxx + dX2_current 
    Syy = Syy + dY2_current 


print( table )
print( f"Avg X : { round( X_avg , round_precision ) }" )
print( f"Avg Y : { round( Y_avg , round_precision ) }" )
print( f"Sxx : { round( Sxx , round_precision ) }" )
print( f"Syy : { round( Syy , round_precision ) }" )
print( f"Sxy : { round( Sxy , round_precision ) }" )

print( "Linear regretion coeffiecients: " ) 
B_hat = Sxy / Sxx
A_hat = Y_avg - B_hat * X_avg 
print( f"B_hat : { B_hat }" )
print( f"A_hat : { A_hat }" )





