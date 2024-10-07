"""
ASSIGNMENET:
    
Write a Python program that generates the running product of elements in an iterable.

https://www.w3resource.com/python-exercises/itertools/index.php

"""

def runningProduct( list ):
    
    tmp = 1
    
    for element in list:
        
        tmp = tmp * element
        print( str( tmp ) )


if __name__ == "__main__":
    
    list = [1, 2 ,3, 4, 5 ,6, 7, 8, 9 ]
    runningProduct( list )
    
    
    
    