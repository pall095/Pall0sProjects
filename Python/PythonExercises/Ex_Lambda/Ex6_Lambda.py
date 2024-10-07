"""
ASSIGNEMENT

Write a Python program to square and cube every number in a given list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

https://www.w3resource.com/python-exercises/lambda/index.php

"""


if __name__ == "__main__": 
    
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print( "La list dei quadrati: " )
    print( list( map( lambda x : x**2 ,  original_list) ) )
    
    print( "La list dei cubi: " )
    print( list( map( lambda x : x**3 ,  original_list) ) )