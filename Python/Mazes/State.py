from enum import Enum

class State( Enum ) :

    FREE = 0 
    WALL = 1 
    START = 2
    END = 3 
    EXPANDED = 4
    SOLUTION = 5 