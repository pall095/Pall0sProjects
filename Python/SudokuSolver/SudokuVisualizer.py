


import tkinter as tk

class SudokuVisualizer:
    
    def __init__(self ):
        self.grid = list( )
        self.cell_size = 50
        self.window_size = self.cell_size * 9

        self.root = tk.Tk()
        self.root.title("Sudoku Grid")

        self.canvas = tk.Canvas(self.root, width=self.window_size, height=self.window_size)
        self.canvas.pack()
        self.root.mainloop()

    def update_grid( self , new_grid ) :
        self.canvas.delete( "all" )
        self.grid = new_grid
        self.draw_grid( )
        self.root.update( )

    def draw_grid(self):
        for i in range(10):  # Grid lines
            width = 3 if i % 3 == 0 else 1
            self.canvas.create_line(0, i * self.cell_size, self.window_size, i * self.cell_size, width=width)
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.window_size, width=width)

        for row in range(9):
            for col in range(9):
                value = self.grid[row][col]
                if value != 0:
                    x = col * self.cell_size + self.cell_size // 2
                    y = row * self.cell_size + self.cell_size // 2
                    self.canvas.create_text(x, y, text=str(value), font=("Arial", 18))
