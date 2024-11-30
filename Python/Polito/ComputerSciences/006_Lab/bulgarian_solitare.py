import random as rd

def generate_inital( ) :
     
    initial_l = rd.randint( 1 , 9 )
    remaining_cards = 45  
    inital_piles = [ ]
    for i in range( initial_l - 1 ) :
        new_pile = rd.randint( 1 , remaining_cards ) 
        remaining_cards = remaining_cards - new_pile 
        inital_piles.append( new_pile ) 
        if remaining_cards == 0 :
            return inital_piles 
    inital_piles.append(  remaining_cards )
    return inital_piles 



def is_final( pile ):
    if len( pile ) != 9 :
        return False
    final_setup = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
    if pile == final_setup :
        return True 
    return False

def generate_new_pile( pile ) :
    new_piles = [ ]
    new_pile_value = 0 
    for i in range( len( pile  ) ) :
        pile[ i ] = pile[ i ] - 1
        new_pile_value += 1 
        if pile[ i ] != 0 :
            new_piles.append( pile[ i ] )     
    new_piles.append( new_pile_value ) 
    return new_piles 

pile = generate_inital( ) 
print( pile )
input( )
while not( is_final( pile ) ) :

        pile = generate_new_pile( pile ) 
        print( pile )


        
        


