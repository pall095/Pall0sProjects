

def find_match( guessed_numbers , winning_list ) :
    num_match = 0 
    for number in guessed_numbers :
        if number == "*" :
            num_match = num_match + 1 
        else:
            if number in winning_list :
                num_match = num_match + 1 

    return num_match 

def list_to_string( guessed_numbers ) :

    string = "" 
    for number in guessed_numbers :

        string = string + number + " "
    return string 



prize_db = dict( )
winning_list = list( )

with open( "prizes.txt" , "r" ) as prize_file :

    for line in prize_file :
        line = line.rstrip( )
        num , prize = line.split( " " ) 
        prize_db[ int( num ) ] = int( prize )

with open( "winning_numbers.txt" , "r" ) as winning_file :

    for line in winning_file :
        line = line.rstrip( )
        line = line.split( " " )
        for number in line : 
            winning_list.append( number ) 

        
with open( "tickets.txt" , "r" ) as ticket_file :

    total_gain = 0 

    for line in ticket_file :
        line = line.rstrip( )
        line = line.split( sep = "," ) 
        ticket_id = line[ 0 ] 
        guessed_numbers = line[ 1 : 7 ]
        total_gain = total_gain + float( line[ 7 ] ) 
        
        num_match = find_match( guessed_numbers , winning_list ) 

        if num_match != 0 :
            if prize_db[ num_match ] != 0 :
                print( f"Ticket ID { ticket_id } Numbers guessed : { list_to_string( guessed_numbers ) } Winning : { prize_db[ num_match ] } prize type { num_match }")
                total_gain = total_gain - prize_db[ num_match ]

    print( f"The total gain is { total_gain }")
