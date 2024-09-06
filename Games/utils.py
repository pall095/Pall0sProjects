import math


def dist( c1 , c2 ) :   
    return math.sqrt(( c1.xc - c2.xc ) **2 + ( c1.yc - c2.yc ) ** 2 )

def gravityComp( c_center , c ) :
    
    xc_rescaled = c.xc - c_center.xc
    yc_rescaled = c.yc - c_center.yc
    
    angle = math.atan2( yc_rescaled , xc_rescaled )
    x_comp = - math.cos( angle )
    y_comp = - math.sin( angle )
    module = gravityModule( c_center, c )
    
    
    print( f"X_comp : {x_comp * module} " )
    print( f"Y_comp : {y_comp * module} " )
    
    return x_comp*module , y_comp*module

def gravityModule( c_center , c ) :
    try :
        return c_center.mass * c.mass / dist( c_center , c ) ** 2     
    except ZeroDivisionError :
        return 0

        