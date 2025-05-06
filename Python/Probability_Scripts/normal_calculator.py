import argparse 
import utils as utl
from scipy.stats import norm

parser = argparse.ArgumentParser( )

parser.add_argument( "mean" , type = float , default = 0 )
parser.add_argument( "std_dev" , type = float , default = 1)
parser.add_argument( "value" , type = float ) 
parser.add_argument( "--round_precision" , type = int , default = 5 )

args = parser.parse_args( )

mean = args.mean 
std_dev = args.std_dev 
value = args.value 
round_precision = args.round_precision

n = norm( mean , std_dev )
print( round( n.cdf( value ) , round_precision ) )


