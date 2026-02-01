import math


def eval( current_comb , use_int = True ) :

    X0 = current_comb[ 0 ]
    Y0 = current_comb[ 1 ]
    I = current_comb[ 2 ]

    X1 = ( not( I ) and not( X0 ) and Y0 ) or ( I and X0 and not( Y0 ) )
    Y1 = I
    Z = I and X0 and not( Y0 )

    if use_int : 
        X0 = int( X0 )
        Y0 = int( Y0 )
        I = int( I )
        X1 = int( X1 )
        Y1 = int( Y1 )
        Z = int( Z )

        print( f" X0: { X0 } - Y0: { Y0 } - I: { I } | X1: { X1 } - Y1: { Y1 } - Z: { Z } - ")



def eval_r ( current_comb , values , combin_len , depth ) :

    if depth >= combin_len :
        eval( current_comb )
        return 

    for value in values :
        current_comb[ depth ] = value 
        eval_r( current_comb , values , comb_len , depth + 1 )


if __name__ == "__main__" :

    values = [ False , True ] 
    num_states_vars = 2
    num_input = 1 

    comb_len = num_states_vars + num_input 
    current_comb = [ False ] * comb_len

    eval_r( current_comb , values , comb_len , 0 )

    
    

