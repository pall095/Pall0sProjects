


time_zone_dict = dict( ) 


with open( "timezones.lst" , "r" ) as timezone_file :
    for line in timezone_file :
        line = line.rstrip( )

        timezone , delta , dump = line.split( " " , maxsplit = 2) 
        timezone = timezone.rstrip( ":" ) 
        
        delta = delta.strip ("UTC" )

        if ":" in delta :
            hr , min = delta.split( ":")
            hr = int( hr ) * 60 

            if hr > 0 :
                delta = hr + int( min ) 
            else :
                delta = -( abs( hr ) +  int( min ) )     
        else :
            delta = int( delta ) * 60 
        time_zone_dict[ timezone ] = delta

    

with open( "today.lst" , "r" ) as event_file :

    for line in event_file :

        line = line.rstrip( )
        current_time , zone , text = line.split( " " , maxsplit = 2 )
        current_hr , current_min = current_time.split( ":" ) 
        current_hr = int( current_hr ) * 60 
        current_min = int( current_min) 
        current_time = current_hr + current_min 

        local_time = current_time - time_zone_dict[zone]


        if local_time < 0 :
            print( f"Yesterday { 24 + local_time//60 }:{ local_time%60 } {text}" )
        elif local_time > 24*60:
            print( f"Tomorrow { local_time//60 - 24 }:{ local_time%60 } {text}")
        else:
            print( f"Today { local_time//60}:{ local_time%60 } {text}")



