"""
ASSIGNEMENT
Write a Python program to filter a list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]

https://www.w3resource.com/python-exercises/lambda/index.php

"""


if __name__ == "__main__":
    
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    
    print( "I numeri pari sono: " )
    print( list( filter( lambda x: x % 2 ==  0 , original_list ) ) )
    
    
    print( "I numeri dispari sono: " )
    print( list( filter( lambda x: x % 2 != 0 , original_list ) ) )
    
   