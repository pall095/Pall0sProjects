import tkinter as tk
from tkinter import ttk
import app_config as _APPCONFIG    
from solve_wrapper import *
import time



MIN = 10 
MAX = 40
STEP = 10 
AVG_WINDOW = 3 

CELL_SIZE = 10 
GEN_METHOD = "random"
SOLVE_METHOD = "Astar Euclidean"
WALL_TH = 0.7
stat_dict = dict( )


for row in range( MIN , MAX + STEP , STEP ) :

    stat_dict[ row ] = dict( )

    for col in range( MIN , MAX + STEP  , STEP ) :
        stat_dict[ row ][ col ] = {
            "values" : list( ) ,
            "avg" : -1  
        }
        for i in range( 0 , AVG_WINDOW , 1  ) :
            start = time.time( )
            solve_maze( ROW = row ,
                        COL = col ,
                        CELL_SIZE = CELL_SIZE , 
                        generation_method = GEN_METHOD ,
                        solving_method = SOLVE_METHOD , 
                        save_output = False ,  
                        wall_thr = WALL_TH ,
                        autoclose = True )
            exec_time = time.time( ) - start
            stat_dict[ row ][ col ][ "values" ].append( exec_time )
        avg_exec = sum( stat_dict[ row ][ col ][ "values" ] ) / len( stat_dict[ row ][ col ] )
        stat_dict[ row ][ col ][ "avg" ] = avg_exec
        
for row in range( MIN , MAX + STEP , STEP ) :
    for col in range( MIN , MAX + STEP , STEP ) :
        print( f"Num Rows : { row } - Num Cols : { col } - Values : { stat_dict[ row ][ col ][ 'values' ] } - Avg : { stat_dict[ row ][ col ][ 'avg' ] }" )
