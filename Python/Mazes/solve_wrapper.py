from tkinter import *
#from Grid import Grid
from Grid import Grid
from Cell import Cell
import datetime
            
def solve_maze( ROW , COL , CELL_SIZE , generation_method , solving_method , save_output , wall_thr , autoclose = False ) :

    grid = Grid( ROW , COL , CELL_SIZE , wall_thr )
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

    if autoclose :
        print( "Destroying")
        grid.ROOT.destroy( )
        
    grid.ROOT.mainloop()



# DEBUG
# Used to run the solution computation without running the app.
if __name__ == "__main__" :
    solve_maze( 100 , 100 , 30 , "random" , "Depth First" , False , 0.7 )
    #solve_maze( 10 , 15 , "from file" , "Astar Euclidean" , False , 0.7 )
        
        
        
        