from tkinter import *
from Grid import Grid
from Cell import Cell
import time
import argparse

ROW = 100
COL = 100
WIDTH = 950
HEIGHT = 950
WALL_THR = 0.8
Cell.ROW = ROW
Cell.COL = COL
Cell.WIDTH = WIDTH
Cell.HEIGHT = HEIGHT    
Grid.WIDTH = WIDTH
Grid.HEIGHT = HEIGHT

Grid.WALL_THR = WALL_THR

#state enum
# 0 : free
# 1 : wall
# 2 : start
# 3 : end
# 4 : expanded
            
if __name__ == '__main__' :
    

    root = Tk( )
    canvas = Canvas( root , width = WIDTH , height = HEIGHT )
    parser = argparse.ArgumentParser( ) 
    parser.add_argument( "method" , choices = [ "Astar_euclidean" , "breath" , "depth" , "man" , "rand"] , help = "Search method" )
    parser.add_argument( "--output" , dest = "output_flag" , action = "store_true" )
    parser.add_argument( "--no_output" , dest = "output_flag" , action = "store_false" )
    parser.set_defaults( output_flag = False )
    parser.add_argument( "--wall_thr" , default = 0.9 , type = float  ) 
    args = parser.parse_args( )
    grid = Grid( ROW , COL , args.wall_thr )
    grid.CANVAS = canvas
    grid.ROOT = root 
    grid.generateMaze( method = "random" )
    #grid.saveMaze( "mazeMaster.txt" )
    #grid.loadMaze( "mazeMaster.txt")
    solveState = 0 

    while solveState == 0 :
        
         solveState = grid.solveStep( method = args.method, showOutput = args.output_flag ) 
     
 
    if solveState == -1 :
        print( "Maze not solvable")
        
    if solveState == 1 :
        print( "Solving method:" + args.method ) 
        print( "Number of expanded nodes: " + str( grid.expandedNodes ) )
        
    root.mainloop()
        
        
        
        