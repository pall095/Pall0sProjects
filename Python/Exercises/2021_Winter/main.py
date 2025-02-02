def is_before( db_date , date ) :

    db_day , db_month , db_year = db_date.split( "-" ) 
    date_day , date_month , date_year = date.split( "-" )

    if int( db_year ) < int( date_year ) :
        return True
    
    elif int( db_year ) == int( date_year ) :

        if int( db_month ) < int( date_month ) :
            return True 
        elif int( db_month ) == int( date_month ) :
            if int( db_day ) < int( date_day ) :
                return True 
            else:
                return False 
        else :
            return False
    else :
        return False 


def find_valid( date , rules_dict ) :

    valid_rules = list( ) 

    for db_date in rules_dict.keys( ) :
        if is_before( db_date , date ) :
            rules = rules_dict[ db_date ] 

            for rule in rules : 
                if rule[ 0 ] == "+" :
                    rule = rule.replace( "+" , "" )
                    if rule not in valid_rules :
                        valid_rules.append( rule )
                elif rule[ 0 ] == "-" :
                    rule = rule.replace( "-" , "" )
                    if rule in valid_rules :
                        valid_rules.remove( rule.replace( "-" , "" ) )
    return valid_rules



rules_dict = dict( )


with open( "rules-example1.dat" , "r" ) as rules_db:

    for line in rules_db :

        line = line.rstrip( )
        date , rules = line.split( ": " ) 
        rules = rules.split( " "  )
        rules_dict[ date ] = rules
        
with open( "dates-example1.dat" , "r" ) as dates_file :

    for line in dates_file :
        date = line.rstrip( )    

        valid_rules = find_valid( date , rules_dict )
        print( f"Rules valid for date { date } are { valid_rules }")


