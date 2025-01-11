import time
import argparse


if __name__ == "__main__" :

    parser = argparse.ArgumentParser( )
    parser.add_argument( "n" )
    args = parser.parse_args( ) 
    start = time.time( ) 
    
    n = int( args.n ) 

    for i in range( n ) :
        continue 


    end = time.time( ) 
    print( f"Time taken : { end - start } s" ) 