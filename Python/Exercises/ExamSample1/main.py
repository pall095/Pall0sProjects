

hotel_dict = dict( ) 
NAME_KEY = 0 
TOT_ROOMS_KEY = 1
PRICE_KEY = 2 
AVAILABLE_ROOMS = 3 

total_confirmed = 0 
total_refused = 0
most_available = 0
max_key = ""


with open( "hotels.txt" , "r" ) as hotel_file :

    for line in hotel_file :
        line = line.rstrip( ) 
        htl_id , htl_name , htl_rooms , htl_price = line.split( ":" ) 
        hotel_dict[ htl_id ] = [ htl_name , int( htl_rooms ) , float( htl_price ) , int( htl_rooms ) ]


with open( "bookings.txt" , "r" ) as booking_file :

    for line in booking_file :
        line = line.rstrip( ) 
        book_id , htl_id , num_rooms = line.split( " " ) 
        num_rooms = int( num_rooms )

        if hotel_dict[ htl_id ][ AVAILABLE_ROOMS ] >= num_rooms :
            print( f"Booking { book_id } CONFIRMED!" )
            hotel_dict[ htl_id ][ AVAILABLE_ROOMS ] = hotel_dict[ htl_id ][ AVAILABLE_ROOMS ] - num_rooms 
            total_confirmed = total_confirmed + 1
        else :
            print( f"Booking { book_id } REFUSED!")
            total_refused = total_refused + 1 

for key , item in hotel_dict.items( ) :

    print( f"Hotel { item[ NAME_KEY ] } rooms : { item[ TOT_ROOMS_KEY ] } ( { item[ AVAILABLE_ROOMS ] } available).")

    if item[ AVAILABLE_ROOMS ] > most_available :
        most_available = item[ AVAILABLE_ROOMS ]
        max_key = key

print( f"The hotel with the largest amount of avaialble rooms is : { hotel_dict[max_key ][ NAME_KEY ] }")
