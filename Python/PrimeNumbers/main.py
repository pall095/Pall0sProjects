
from datetime import datetime

prime_list = [ 1 , 2 ]
max_num = 10000
current_number = 3 
is_current_prime = True


start = datetime.now( )
while len( prime_list ) < max_num :
         
        for prime in prime_list :           
            if current_number % prime == 0 and prime != 1 :           
                is_current_prime = False
                break
            
        if is_current_prime :
            print( f"New prime found: {current_number}")
            prime_list.append( current_number )
        else :
            is_current_prime = True
            
        current_number = current_number + 2 #Vado solo attraverso i dispari. Per funzionare devi avere già 1 e 2 nella lista.
        
        
print( f"Time : { datetime.now() -  start }")
                


