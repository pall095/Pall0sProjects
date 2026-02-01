from prettytable import PrettyTable
import time

class SudokuSolver( ) :

    def __init__(self ) :

        self.grid = list( )
        self.size = 9
        self.block_size = 3
        self.solved = False
        self.speed = 0.0005
        self.pretty_table = PrettyTable( ) 
        self.pretty_table.field_names = [ i for i in range( 1 , self.size + 1 ) ]


    def solve_r( self , output ) :

        if output: 
            self.print_pretty_grid( )

        if self.is_solved( ) :
            self.solved = True 
            return
    
        for row in range( self.size ):
            for col in range( self.size ) :
                if self.grid[ row ][ col ] == 0 :
                    for current_num in range( 1 , self.size + 1) :
                        if self.is_valid( row , col , current_num ) :
                            self.grid[ row ][ col ] = current_num
                            self.solve_r( output )

                            if self.solved :
                                return 

                            self.grid[ row ][ col ] = 0
                    return

                        

    def is_valid( self , row , col , current_num ) :
        return self.check_row( row , current_num ) and self.check_col( col , current_num ) and self.check_block( row , col , current_num )
    

    def check_row( self , row , current_num ) :
        return current_num not in self.grid[ row ]
    
    def check_col( self , col , current_num ) :
        composed_col = [ row[ col ] for row in self.grid ]
        return current_num not in composed_col
    
    def check_block( self , row , col , current_num ) :

        row_start = row // self.block_size * self.block_size
        col_start = col // self.block_size * self.block_size

        for sub_row in range( self.block_size ) :
            for sub_col in range( self.block_size ) :
                if current_num == self.grid[ row_start + sub_row ][ col_start + sub_col ] :
                    return False

        return True


    def is_solved( self ) :

        for i in range( self.size ) :
            if 0 in self.grid[ i ] :
                return False
        return True
            
    def parse_grid_from_file( self , filepath ) :
        with open( filepath , "r" ) as input_grid :
            for line in input_grid :        
                    line = line.rstrip( )
                    self.grid.append( list( int( x ) for x in line ) )
            

    def print_pretty_grid( self ) :
        
        self.pretty_table.clear_rows( )
        for i , row in enumerate( self.grid ) :

            if i % 3 == 0 and i != 0 :
                self.pretty_table.add_row( [ "-" for _ in range( 9 ) ] )
            row_display = [ " " if value == 0 else value for value in row ]
            self.pretty_table.add_row( row_display )
        
        print( self.pretty_table )
        time.sleep( self.speed )

    def print_grid( self ) :
        
        for row in range( self.size ) :
            for col in range( self.size ) :
                print( f"{ self.grid[ row ][ col ] }" , end = " " )
            
            print( )
    
     







