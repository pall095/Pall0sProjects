"""

Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
Sample Output:
25
48

https://www.w3resource.com/python-exercises/lambda/index.php

"""


if __name__ == "__main__":
    
    value = 10
    multiplier = 10
    fun1 = ( lambda: value + 15 )
    fun2= ( lambda multiplier: value * multiplier)
    
    print( "Value + 15: " + str( fun1( ) ) )
    print( "Value * " + str( multiplier ) + ": " + str( fun2( multiplier ) ) )