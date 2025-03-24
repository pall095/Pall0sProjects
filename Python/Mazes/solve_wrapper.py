from tkinter import *
#from Grid import Grid
from Grid import Grid
from Cell import Cell
import datetime
            
def solve_maze( ROW , COL , generation_method , solving_method , save_output , wall_thr ) :

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

    root = Tk( )
    canvas = Canvas( root , width = WIDTH , height = HEIGHT )
    grid = Grid( ROW , COL , wall_thr )
    grid.CANVAS = canvas
    grid.ROOT = root 
    grid.generateMaze( method = generation_method )
    solve_suffix = ""

    solveState = 0 

    while solveState == 0 :
        solveState = grid.solveStep( method = solving_method , showOutput = False ) 
     
    
    if solveState == -1 :
        print( "Maze not solvable")
        solve_suffix = "_KO"
        
    if solveState == 1 :
        print( "Solving method:" + solving_method ) 
        print( "Number of expanded nodes: " + str( grid.expandedNodes ) )
        solve_suffix = "_OK"

    if save_output :
        now = datetime.datetime.now( )
        output_file = "output_mazes/" + now.strftime("%Y-%m-%d_%H%M%S_out") + solve_suffix + ".txt"  
        grid.saveMaze( output_file )
        
    root.mainloop()
        
        
        
        