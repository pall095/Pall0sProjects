import argparse 
import utils as utl


def calculate_binom_value( num_trials , num_success , probability , round_precision , verbose ) -> float :
    binomial_coefficient = utl.fact( num_trials ) / ( utl.fact( num_success ) * utl.fact( num_trials - num_success ) ) 
    result = round( binomial_coefficient * probability ** ( num_success ) * ( 1 - probability ) ** ( num_trials - num_success ) , round_precision )
    if verbose :
        print( f"Calculating for { num_success } - Probability : { result  }" )

    return result 

parser = argparse.ArgumentParser( )

parser.add_argument( "num_trials" , type = int )
parser.add_argument( "probability" , type = float )
parser.add_argument( "mode" , choices = [ "equal" , "less" , "leq" , "greater" , "geq" ] )
parser.add_argument( "num_success" , type = int ) 
parser.add_argument( "--round_precision" , type = int , default = 5 )
parser.add_argument( "--verbose" , action = "store_true" ) 

args = parser.parse_args( )

num_trials = args.num_trials 
probability = args.probability 
num_success = args.num_success 
round_precision = args.round_precision
mode = args.mode 
verbose = args.verbose

if mode == "equal" :
    success_list = [ num_success ]

elif mode == "less" :
    success_list = [ x for x in range( 0 , num_success ) ]

elif mode == "leq" :
    success_list = [ x for x in range( 0 , num_success + 1 ) ]

elif mode == "geq" :
    success_list = [ x for x in range( num_success , num_trials + 1 ) ]

elif mode == "greater" :
    success_list = [ x for x in range( num_success , num_trials + 1 ) ]

value = map( lambda num_success_tmp : calculate_binom_value( num_trials , num_success_tmp , probability , round_precision , verbose ) , success_list )
print( sum( value ) )




