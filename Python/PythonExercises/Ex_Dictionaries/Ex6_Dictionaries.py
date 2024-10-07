"""
ASSIGNEMENT:

Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

https://www.w3resource.com/python-exercises/dictionary/

"""

if __name__ == "__main__" :
    
    number = 5 
    dic = { }
    
    
    for i in range( 1 , number + 1 ):
        
        tmp = { i : i*i }
        dic.update( tmp )
        
        
    print( dic )
    
 