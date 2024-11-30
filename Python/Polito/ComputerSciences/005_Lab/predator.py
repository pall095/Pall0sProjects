
# CONSTANT DEFINITION
A = 0.1
B = 0.01
C = 0.01
D = 0.0002

X = 1000
Y = 20

num_iter = 100 

for i in range( num_iter ) :

    print( f"Itertion { i } : preys - { X } -  predators - { Y } " )

    X = X * ( 1 + A - B * Y ) 
    Y = Y * ( 1 - C + D * Y )