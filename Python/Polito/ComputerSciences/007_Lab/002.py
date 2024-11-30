

number_list_vanilla = input( "Insert the list of number separated by : " )
number_list_values = number_list_vanilla.split( ":" ) 
for i in range( len( number_list_values ) ) :

    number_list_values[ i ] = int( number_list_values[ i ] )

no_max_min_string = ""
only_even_string = "" 
two_digit_string = "" 

for number in number_list_values :
    if number != max( number_list_values ) and number != min( number_list_values ) :
        no_max_min_string = no_max_min_string + str( number ) + ":"
    if number%2 == 0 :
        only_even_string = only_even_string + str( number ) + ":"

    if number >= 10 :
        two_digit_string = two_digit_string + str( number ) + ":" 

print( no_max_min_string.rstrip( ":" ) )
print( only_even_string.rstrip( ":") )
print( two_digit_string.rstrip( ":" ) )







