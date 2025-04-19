import pygame
import planet_schema as _PLANET_CONFIG


class Circle:
    
    vectorMultiplier = 2 
    
    def __init__( self , name , rgb , mass , radius , xc , yc , vx , vy , ax , ay , collision_flag , gravity_flag ) :
              
        self.name = name
        self.mass = mass
        self.xc = xc
        self.yc = yc
        self.speed_x = vx
        self.speed_y = vy
        self.acc_x = ax
        self.acc_y = ay
        
        self.check_collision = collision_flag
        self.check_gravity = gravity_flag
        
        self.r = radius
        if isinstance( rgb , list ) :
            self.rgb = rgb 
        else :
            red , green , blue = rgb.split( _PLANET_CONFIG.RGB_DELIMITER ) 
            self.rgb = [ int( red ) , int( green ) , int( blue ) ]


    # Alternative 
    @classmethod
    def init_from_dict( cls , dict ) :

        name = dict[ _PLANET_CONFIG.NAME_KEY ] 
        rgb = dict[ _PLANET_CONFIG.RGB_KEY ]
        mass = dict[ _PLANET_CONFIG.MASS_KEY ]
        radius = dict[ _PLANET_CONFIG.RADIUS_KEY ]
        
        xc = dict[ _PLANET_CONFIG.INITIAL_POS_X_KEY ]
        yc = dict[ _PLANET_CONFIG.INITIAL_POS_Y_KEY ]

        speed_x = dict[ _PLANET_CONFIG.INITIAL_SPEED_X_KEY ]
        speed_y = dict[ _PLANET_CONFIG.INITIAL_SPEED_Y_KEY ]

        acc_x = dict[ _PLANET_CONFIG.INITIAL_ACC_X_KEY ]
        acc_y = dict[ _PLANET_CONFIG.INITIAL_ACC_X_KEY ]
        
        check_collision = dict[ _PLANET_CONFIG.CHECK_COLLISION_KEY ]
        check_gravity = dict[ _PLANET_CONFIG.CHECK_GRAVITY_KEY ]

        circle = Circle( name , rgb , mass , radius , xc , yc , speed_x , speed_y , acc_x , acc_y , check_collision , check_gravity )
        return circle
        
        
    def printState( self ) :
        
        print( f"X : { self.xc } - Y : { self.yc } - Vx : { self.speed_x } - Vy : { self.speed_y } - Ax : { self.acc_x } - Ay : { self.acc_y }" )
    

    def print_state( self ) :
        
        print( f"Name: {self.name}" )
        print( f"Position : x = {self.xc} - y = {self.yc}" )
        print( f"Speed : x = {self.speed_x} - y = {self.speed_y}" )
        print( f"Position : x = {self.acc_x} - y = {self.acc_y}" )
        print( "---")
    
        
        
    def update_speed( self ) :
        self.speed_x = self.speed_x + self.acc_x
        self.speed_y = self.speed_y + self.acc_y

    def impose_speed( self , new_speed  : list  ) : 
        self.speed_x = new_speed[ 0 ]
        self.speed_y = new_speed[ 1 ]
            
    
    def impose_acc( self , new_acc : list ) :
        self.acc_x = new_acc[ 0 ]
        self.acc_y = new_acc[ 1 ]
        
    def update_acc( self , new_acc : list ) :
            self.acc_x = self.acc_x + new_acc[ 0 ] 
            self.acc_y = self.acc_y + new_acc[ 1 ] 
            
    def update_pos( self ) :
        
        self.xc = self.xc + self.speed_x
        self.yc = self.yc + self.speed_y
        
    def impose_pos( self , new_pos : list ) :
        self.xc = new_pos[ 0 ]
        self.yx = new_pos[ 1 ]

    def offset_pos( self , offset : tuple ) :
        self.xc = self.xc + offset[ 0 ]
        self.yc = self.yc + offset[ 1 ]     
                        
    
    def update( self ) :
        self.update_speed( )
        self.update_pos( )
        
        if self.check_collision :
        
            if ( self.xc + self.speed_x + self.r ) > self.screen.get_width( ) or ( self.xc + self.speed_x - self.r ) <= 0:
                self.speed_x = -self.speed_x
    
            if ( self.yc + self.speed_y + self.r ) > self.screen.get_height() or ( self.yc + self.speed_y - self.r ) <= 0:
                self.speed_y = -self.speed_y
            

    def get_speed_vector( self , rescale_factor ) -> tuple :
        return ( self.xc + self.speed_x * rescale_factor , self.yc + self.speed_y * rescale_factor )    
    
    def get_acc_vector( self , rescale_factor ) -> tuple :
        return ( self.xc + self.acc_x * rescale_factor , self.yc + self.acc_y * rescale_factor  )

    def get_radius( self ) :
        return self.r 
        
    def get_current_pos( self ) -> tuple :
        return ( self.xc , self.yc )
        
    def center_to_list( self ) :
        return [ self.xc , self.yc ]