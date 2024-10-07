"""
ASSIGNEMENT:

Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

https://www.w3resource.com/python-exercises/dictionary/

"""


if __name__ == "__main__" :
    
    dic1 = {1:10, 2:20}
    dic2 = {3:30, 4:40}
    dic3 = {5:50,6:60}
    
    out_dic = { }

    for d in ( dic1 , dic2 , dic3 ) :
        
        out_dic.update( d )


    print( out_dic )
    
    
    
    