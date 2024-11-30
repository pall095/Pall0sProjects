


def reformat_time( local_time , delta_time ) :

    day = "Today"

    if ":" in local_time :
        local_time_hr , local_time_min = local_time.split( ":" )
    else:
        local_time_hr = local_time 
        local_time_min = 0 

    if ":" in delta_time :
        delta_time_hr , delta_time_min = delta_time.split( ":" )
    else :
        delta_time_hr = delta_time 
        delta_time_min = 0 

    local_time_hr = int( local_time_hr ) 
    local_time_min = int( local_time_min ) 
    delta_time_hr = int( delta_time_hr ) 
    delta_time_min = int( delta_time_min ) 

    if delta_time_hr < 0 :
        delta_time_min = -delta_time_min 

    new_time_hr = local_time_hr - delta_time_hr 
    new_time_min = local_time_min - delta_time_min 


    if new_time_min > 60 :
        new_time_hr = new_time_hr + new_time_min//60 
        new_time_min = new_time_min%60 
    elif new_time_min < 0 :
        new_time_hr = new_time_hr - abs(new_time_min)//60 - 1
        new_time_min = 60 - abs( new_time_min )%60

    if new_time_hr > 24 :
        day = "Tomorrow" 
        new_time_hr = new_time_hr%24
    elif new_time_hr < 0 :
        day = "Yesterday" 
        new_time_hr = 24 + new_time_hr 

    return [ day , new_time_hr , new_time_min ]
    

    


time_zone_dict = dict( )

with open( "timezones.lst" , "r" ) as time_zone_info :


    for line in time_zone_info :

        line = line.rstrip( )
        timezone , delta , dump = line.split( " " , maxsplit = 2 ) 
        
        timezone = timezone.rstrip( ":" ) 
        delta = delta.replace( "UTC" , "" )     
        time_zone_dict[ timezone ] = delta 

time_zone_info.close( )


with open( "today.lst" , "r" ) as today_file :

    for line in today_file :
        local_time , timezone , text = line.split( " " , maxsplit = 2 )


        if timezone in time_zone_dict.keys( ) :
            [ day , new_time_hr , new_time_min ] = reformat_time( local_time , time_zone_dict[ timezone ] )
            print( f"{ day } { new_time_hr }:{ new_time_min } { text.rstrip( )}" ) 









            

            
            
             





            

        


