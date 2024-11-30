R0 = 20 
Vs = 20 
Rs = 80

n = 0.01 
increment = 0.01
speraker_power_max = 0 
n_max = 0 

while n <= 2 + increment  :
    
    speraker_power = Rs *( n*Vs / ( n**2 *R0 + Rs ) ) **2 
    print( f"Power delivered to the speaker with { n } turn ratio : {speraker_power}" )

    if speraker_power > speraker_power_max :
        speraker_power_max = speraker_power 
        n_max = n 

    n = n + increment 

print( f"The turn ratio that maximizes the power is {n_max}")
