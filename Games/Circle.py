import pygame



class Circle:
    
    vectorMultiplier = 2 
    
    def __init__( self , screen , name , initial_pos : list , r , mass , rgb : list , speed = [ 0, 0 ] , acc = [ 0 , 0 ] , check_collision = False , check_gravity = True ) :
        
        self.name = name 
        self.xc = initial_pos[ 0 ]
        self.yc = initial_pos[ 1 ]
        self.r = r
        self.mass = mass
        
        self.speed_x = speed[ 0 ]
        self.speed_y = speed[ 1 ]
        
        self.acc_x = acc[ 0 ]
        self.acc_y = acc[ 1 ]
        
        self.screen = screen
        self.check_collision = check_collision 
        self.check_gravity = check_gravity
        
        self.rgb = rgb
        
        
    def printState( self ) :
        
        print( f"X : { self.xc } - Y : { self.yc } - Vx : { self.speed_x } - Vy : { self.speed_y } - Ax : { self.acc_x } - Ay : { self.acc_y }" )
    
    def drawSpeed( self , rescale_factor = 1 ) :
        pygame.draw.line( self.screen , [0 , 255 , 0 ] , ( self.xc , self.yc ) , ( self.xc + self.speed_x * rescale_factor , self.yc + self.speed_y * rescale_factor ) )
    
    def drawAcc( self , rescale_factor ) :
        
        pygame.draw.line( self.screen , [255 , 0 , 0 ] , ( self.xc , self.yc ) , ( self.xc + self.acc_x * rescale_factor , self.yc + self.acc_y * rescale_factor ) )
        
    def print_state( self ) :
        
        print( f"Name: {self.name}" )
        print( f"Position : x = {self.xc} - y = {self.yc}" )
        print( f"Speed : x = {self.speed_x} - y = {self.speed_y}" )
        print( f"Position : x = {self.acc_x} - y = {self.acc_y}" )
        print( "---")
    
    
    def draw( self , verbose = False , rescale_factor = 1 ) :
        
        pygame.draw.circle( self.screen, self.rgb , ( self.xc, self.yc ), self.r ) 
        self.drawSpeed( rescale_factor )
        self.drawAcc( rescale_factor ) 
        
        if verbose :    
            self.print_state( )
        
        
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
                        
    
    def update( self ) :
        
        self.update_speed( )
        self.update_pos( )
        
        if self.check_collision :
        
            if ( self.xc + self.speed_x + self.r ) > self.screen.get_width( ) or ( self.xc + self.speed_x - self.r ) <= 0:
                self.speed_x = -self.speed_x
    
            if ( self.yc + self.speed_y + self.r ) > self.screen.get_height() or ( self.yc + self.speed_y - self.r ) <= 0:
                self.speed_y = -self.speed_y
            

        self.draw()
        
        
    def center_to_list( self ) :
        return [ self.xc , self.yc ]