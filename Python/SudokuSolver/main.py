from tkinter import filedialog
from SudokuSolver import SudokuSolver


sudoku_file = filedialog.askopenfilename( title = "Select a sudoku grid" )
solver = SudokuSolver( ) 
solver.parse_grid_from_file( sudoku_file )
solver.solve_r( output = False )

if solver.solved :
    print( "Solved" ) 
    solver.print_pretty_grid( )
else :
    print( "Not solved")