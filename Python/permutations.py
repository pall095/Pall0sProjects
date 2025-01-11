import time
import argparse

def permutations_r( n , sol , marker , depth , cnt , verbose ) :

	if( depth >= n ) :

		if verbose :
			print( sol ) 
		return cnt + 1 

	for i in range( n ) :
		if marker[ i ] == 0 :
			marker[ i ] = 1 
			sol[ depth ]  = i + 1
			cnt = permutations_r( n , sol , marker , depth + 1 , cnt , verbose ) 
			marker[ i ] = 0  
	return cnt 

def permutations( n , verbose ) :

	marker = [ 0 ] * n  
	sol = [ 0 ] * n 
	depth = 0 
	cnt = 0 
	cnt = permutations_r( n , sol , marker , depth , cnt , verbose ) 
	return cnt 

if __name__ == "__main__" :

	parser = argparse.ArgumentParser( )
	parser.add_argument( "n" )
	parser.add_argument( "verbose" )  
	args = parser.parse_args( ) 
	start = time.time( ) 
	cnt = permutations( int( args.n ) , int( args.verbose ) ) 
	end = time.time( ) 
	print( f"Time taken : { end - start } s" ) 
	print( f"Number of permutations: { cnt }" ) 
