from tkinter import *
from Grid import Grid
from Cell import Cell
import time

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
    solvingMethods = [ "Astar_euclidean" , "breath" , "depth" , "man" , "rand"]
    grid = Grid( ROW , COL )
    grid.CANVAS = canvas
    grid.ROOT = root 
    grid.generateMaze( method = "random" )
    #grid.saveMaze( "mazeMaster.txt" )
    #grid.loadMaze( "mazeMaster.txt")
    solveState = 0 
    method = solvingMethods[ 0 ]

    
    while solveState == 0 :
        
         solveState = grid.solveStep( method = method , showOutput = False ) 
     
 
    if solveState == -1 :
        print( "Maze not solvable")
        
    if solveState == 1 :
        print( "Solving method:" + method ) 
        print( "Number of expanded nodes: " + str( grid.expandedNodes ) )
        
    root.mainloop()
        
        
        
        