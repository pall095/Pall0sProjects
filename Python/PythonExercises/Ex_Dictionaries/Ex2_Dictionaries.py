"""

ASSIGNEMENT:

Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
    
https://www.w3resource.com/python-exercises/dictionary/

"""


if __name__ == "__main__" :
    
    d = { 0: 10, 1: 20 }
    new_item = { 2 : 30 }
    
    d.update( new_item )
    
    print( d )
    
