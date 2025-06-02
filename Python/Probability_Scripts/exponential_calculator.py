import argparse 
import utils as utl
import math

INF_KEY = "inf"

parser = argparse.ArgumentParser( )

parser.add_argument( "l" , type = float )
parser.add_argument( "integration_upper" , type = str )
parser.add_argument( "integration_lower" , type = str )
parser.add_argument( "--round_precision" , type = int , default = 2 )

args = parser.parse_args( )

l = args.l
integration_upper = args.integration_upper 
integration_lower = args.integration_lower 
round_precision = args.round_precision

if integration_upper == INF_KEY and not( integration_lower == INF_KEY ) :

    integration_lower = float( integration_lower )
    print( round( math.e ** ( -l * integration_lower ) , round_precision ) ) 

else :
    integration_upper = float( integration_upper )
    integration_lower = float( integration_lower ) 

    term1 = - math.e ** ( -l * integration_upper )
    term2 = - math.e ** ( -l * integration_lower ) 
    print( round( term1 - term2 , round_precision ) )   
















