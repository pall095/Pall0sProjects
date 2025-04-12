import random as rand
from Cell_refactor import Cell
from tkinter import *
from copy import deepcopy
from math import dist
from State_refactor import State
from tkinter.filedialog import askopenfilename
import Grid_config as _CONFIG


class Grid:
    
    WIDTH = 0 
    HEIGHT = 0 
    CANVAS = 0
    ROOT = 0
    CELL_SIZE = 0 
    WALL_THR = 0
    
    def __init__( self , ROW , COL , CELL_SIZE , WALL_THR ) :
        
        self.ROW = ROW 
        self.COL = COL

        while ROW * CELL_SIZE >= _CONFIG.WINDOW_LIMIT or COL * CELL_SIZE >= _CONFIG.WINDOW_LIMIT :
            print( f"Curent cell size of { CELL_SIZE } size will make the window bigger than { _CONFIG.WINDOW_LIMIT }. Rescaling cell size..." )
            CELL_SIZE = int( CELL_SIZE - _CONFIG.REUCTION_FACTOR * CELL_SIZE )

        self.CELL_SIZE = CELL_SIZE
        self.WIDTH = ROW * CELL_SIZE
        self.HEIGHT = COL * CELL_SIZE
        print( f"Final dimension - WIDTH : { self.WIDTH } - HEIGHT : { self.HEIGHT } - CELL_SIZE : { self.CELL_SIZE }" )

        self.CELL_SIZE = CELL_SIZE 
        self.WALL_THR = WALL_THR

        self.ROOT = Tk( )
        self.CANVAS = Canvas( self.ROOT , width = self.WIDTH , height = self.HEIGHT ) 

        self.grid = [ ]
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.queue = [ ]
        self.expandedNodes = 0

        for x in range( self.ROW ) : 
            tmp = [ ]
            for y in range( self.COL ) :              
                tmp.append( Cell( x , y , state = State.FREE , depth = 0 ) )                      
            self.grid.append( tmp )

    
    
    # ----------------------------------- GETTER & SETTER -----------------------------------  #
            
    def getState( self , x , y ) :    
        return self.grid[ x ][ y ].state
    
    def setState( self , x , y , state ) :
        self.grid[ x ][ y ].state = state
        self.updateCell( x , y )
    
    def getCell( self , x , y ) :
        return self.grid[ x ][ y ]
    
    def setDepth( self , x , y , depth ) :
        self.grid[ x ][ y ].depth = depth  
    
    def getDepth( self , x , y ) :
        return self.grid[ x ][ y ].depth 
     
    def setStart( self , new_x , new_y ) :
        
        self.setState( self.start_x , self.start_y , State.FREE )
        self.start_x = new_x 
        self.start_y = new_y
        self.setState( self.start_x , self.start_y , State.START )
        self.queue = [ ]
        self.queue.append( self.getCell( self.start_x , self.start_y ) )


    # ----------------------------------- SOLUTION HANDLING -----------------------------------  #
    
    # Solve the maze step by step, return to main the solving status which is enumerated as follow:
    # 0 - still solving.
    # 1 - succesfully solved.
    # 2 - maze is not solvable.
    # Take as argument the solving method (i.e. how to populate and order the queue) and a boolean to suppress the debug
    # output.
    def solveStep( self , method : str , showOutput : bool ) :

        if len( self.queue ) == 0 :
            print( "Solution not found!" )
            return -1
        else:
            currentCell = self.queue.pop( 0 )             
        if currentCell.state == State.EXPANDED :
            return 0         
        if currentCell.state == State.END :
            print( "SOLVED!  Solution found" )
            self.showSolution( currentCell )
            return 1
        else:
            if showOutput :
                print( "Expanding Node at: " + str( currentCell.row )  + "-" + str( currentCell.col ) )
                print( "Depth: " + str( currentCell.depth ) )
                print( "Cost: " + str( currentCell.cost ) )
                print( "Path:" + str( currentCell.path ) )
                print( "State: " + str( currentCell.state ) )
                print( "---")
            self.expandCell2( currentCell , method )
            self.expandedNodes += 1 
            if currentCell.state != State.START : 
                self.setState( currentCell.row , currentCell.col , State.EXPANDED )
            self.ROOT.update( )
            return 0
        
    # Expand the current node by getting its childrens (up, down, left, right ).
    # Updates the depth and cost (based on the method), and if applicable appends them to the queue.
    # Before "returning", sorts the queue (always by cost).
    def expandCell2( self , cell , method ) :        
        row = cell.row 
        col = cell.col
        path = deepcopy( cell.path )
        offset = [ ( 1 , 0 ) ,  ( 0 , 1 ) , ( -1 , 0 ) , ( 0 , -1 ) ] 
        for off in offset :
            
            temp = self.moveTo( row + off[ 0 ] , col + off[ 1 ] )
            if temp != None : 
                temp.path = path 
                temp.depth = self.getDepth( row , col ) + 1 
                temp.path.append( ( row , col ) )
                temp.cost = temp.depth + self.updateCost( temp.row , temp.col , method )
                if temp.state != State.EXPANDED and temp.state != State.START and temp.state != State.WALL  :
                    self.queue.append( temp )
            else : 
                continue 
        self.updateQueu( method )
        
    # Return the Cell specified by the values of x and y (row and column).
    # Returns None if:
    # - Coordinates are out of bounds.
    # - Cell is a wall.
    # - Cell has already been expanded.
    def moveTo( self , x , y ) :
        
        if x >= self.ROW : return None
        if x < 0 : return None
        if y >= self.COL : return None
        if y < 0 : return None
        if self.getState( x , y ) == State.WALL : return None
        if self.getState( x , y ) == State.EXPANDED : return None    
        return self.getCell( x , y )
    
    # Update the cost of the given cell based on teh method passed as input argument.
    # Since the depth is already updated by default, returns 0 if the method is depth or breath.
    def updateCost( self , x , y , method ) :
    
        if method == "rand" :
            return rand.randint( 0 , 100 )
        if method == "Astar Manhatthan" :
            return abs( x - self.end_x ) + abs( y - self.end_y )  
        if method == "Astar Euclidean" :
            return dist( [ x , y ] ,  [ self.end_x , self.end_y ] )
        if method == "Depth First" or method == "Breath First" :
            return 0
        
    # Sorts the queue based on the search method.
    # By default sorts by cost in ascending order (lowest cost at the beginning)
    def updateQueu( self , method ) :
        
        if method == "Depth First" :
            self.queue.sort( reverse = True , key = lambda item : item.depth )
            
        else:
            self.queue.sort( key = lambda item : item.cost )
            
    
    # ----------------------------------- OUTPUT UPDATE -----------------------------------  #
    
    # Updates a specific output rectangle based on the state of the cell.
    # It is called in "setState", so everytime a cell value is updated, also the output does so.
    def updateCell( self , x , y ) :
        
        x1 = x * self.CELL_SIZE
        y1 = y * self.CELL_SIZE
        color_string = ""
          
        if self.getState( x , y ) == State.FREE :
            color_string = "white"
        elif self.getState( x , y ) == State.WALL :
            color_string = "black"
        elif self.getState( x , y ) == State.START :
            color_string = "green"
        elif self.getState( x , y ) == State.END :
            color_string = "red"
        elif self.getState( x , y ) == State.EXPANDED :
            color_string = "yellow"  
        elif self.getState( x , y ) == State.SOLUTION :
            color_string = "blue"  

        self.CANVAS.create_rectangle( x1 , y1 , x1 + self.CELL_SIZE , y1 + self.CELL_SIZE , fill = color_string )
                       
        self.CANVAS.pack( )
        
    # When the solution is found, update the output to highlight the solution in the window.
    def showSolution( self , cell ) :  
        print( "Solution length: " + str( len( cell.path ) ) )
        for item in cell.path :      
            if not( item[ 0 ] == self.start_x and item[ 1 ] == self.start_y ) : self.setState( item[ 0 ], item[ 1 ] , State.SOLUTION )

    
    # ----------------------------------- MAZE HANDLING -----------------------------------  #
    
    # Master method. Given the grid (self) and the method, calls the appropriate function to 
    # populate the grid.
    def generateMaze( self , method ) :      
        
        if method == "random" :
            return self.generateRandomMaze( )
        
        elif method == "from file" :
            input_file = askopenfilename( title = "Select input file" )
            return self.loadMaze( inputFile = input_file )
        

        
    #Saving the maze
    def saveMaze( self , outputFile ) :      
        f = open( outputFile , 'w' )
        for row in range( self.ROW  ):
            for col in range( self.COL ) :             
                f.write( str( self.getState( row , col ).value ) )
            f.write( "\n" )
        f.close( )
    
    #Loading a maze
    def loadMaze( self , inputFile ) :
        f = open( inputFile , 'r' )     
        row = 0 
        col = 0      
        while 1 :          
            char = f.read( 1 ) 
            if not char : break
            elif char == "\n" : 
                row = row + 1
                self.COL = col 
                col = 0  
            else:
                state = State( int( char ) ) 
                self.setState( row , col , state )               
                if state == State.START :
                    self.start_x = row 
                    self.start_y = col
                    self.queue.append( self.getCell( self.start_x , self.start_y ) )             
                if state == State.END :
                    self.end_x = row
                    self.end_y = col
                col = col + 1               
        self.ROW = row
        f.close( )
                 
    # Random Maze
    def generateRandomMaze( self ) :
        
        for x in range( self.ROW):
            for y in range( self.COL ):
                state_temp = rand.random( )
                if state_temp > self.WALL_THR :
                    self.setState( x , y , State.WALL ) 
                else :
                    self.setState( x , y , State.FREE )
                                   
        start_setted = False
        end_setted = False
        
        while not( start_setted and end_setted ):
            
            start_x = rand.randint( 0 , self.ROW - 1 )
            start_y = rand.randint( 0 , self.COL - 1 )
            
            end_x = rand.randint( 0 , self.ROW - 1 )
            end_y = rand.randint( 0 , self.COL - 1 )
              
            if self.getState( start_x , start_y ) == State.FREE  and not( start_setted ) :
                self.setState( start_x , start_y ,  State.START )
                self.start_x = start_x 
                self.start_y = start_y
                self.queue.append( self.getCell( self.start_x , self.start_y ) )
                start_setted = True
                
            if self.getState( end_x , end_y ) == State.FREE  and not( end_setted ) :
                self.setState( end_x , end_y ,  State.END )
                self.end_x = end_x
                self.end_y = end_y 
                end_setted = True

    # ----------------------------------- UTILITIES -----------------------------------  #

    # Print grid to console as a matrix separated by "-".
    def printGrid( self ) :

       for x in range( self.ROW ) :     
           tmp = ""     
           for y in range( self.COL ) :        
               tmp = tmp + str( self.getState( x , y ) ) + "-"   
           print( tmp )

    # Print queue of cells to be expanded.
    def printQueue( self ) :     
        tmp = ""      
        for item in self.queue :
            
            tmp = tmp + str( round( item.cost ,  2 ) ) + "-"      
        print( tmp )
    
    
    
    
    
    
    
    
    
    
    
    
     

    
            