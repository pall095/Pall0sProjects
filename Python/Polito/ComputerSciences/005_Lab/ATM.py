

num_error = 0
while num_error < 3 :

    pin = input( "Insert pin: " ) 

    if pin == "1234" :
        print( "PIN is corret!" ) 
        break
    else:
        print( "Wrong pin")
        num_error += 1 


if num_error == 3 :
    print( "You bank account is blocked!")

