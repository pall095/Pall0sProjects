
def list_to_string( list_of_stones ) :
     
     for stone in list_of_stones :
          print( stone , end = " " )


location_list = list( ) 
stones_location_db = dict( )

with open( "trips.txt" , "r" ) as trips_file :

    total_duration = 0 
    total_passengers = 0 
    num_trips = 0 

    for line in trips_file :
        line = line.rstrip( )
        location , duration , passengers = line.split( "," ) 

        num_trips = num_trips + 1 
        total_duration = total_duration + int( duration )
        total_passengers = total_passengers + int( passengers ) 
        location_list.append( location )

with open( "stones.txt" , "r" ) as stones_file :
    for line in stones_file :
            line = line.rstrip( )
            location , stones_list = line.split( "," , maxsplit = 1 )
            stones_location_db[ location ] = stones_list 


print( f"The average duration of trips is : { total_duration / num_trips }" )
print( f"The total number of carried passengers is : { total_passengers }" )
print( f"Tiypes of gemstones by place visited : " ) 
for location in location_list :
    
    print( f"{ location }" , end = " " ) 
    print( stones_location_db[ location ] ) 



