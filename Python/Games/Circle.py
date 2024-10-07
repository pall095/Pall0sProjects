import pygame



class Circle:
    
    vectorMultiplier = 2 
    
    def __init__( self , screen , initial_pos : list , r , mass , rgb : list , speed = [ 0, 0 ] , acc = [ 0 , 0 ] , check_collision = False , check_gravity = True ) :
        
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
    
    def drawSpeed( self ) :
        pygame.draw.line( self.screen , [0 , 255 , 0 ] , ( self.xc , self.yc ) , ( self.xc + self.speed_x , self.yc + self.speed_y ) )
    
    def drawAcc( self ) :
        
        pygame.draw.line( self.screen , [255 , 0 , 0 ] , ( self.xc , self.yc ) , ( self.xc + self.acc_x , self.yc + self.acc_y ) )
        
    def draw( self ) :
        
        pygame.draw.circle( self.screen, self.rgb , ( self.xc, self.yc ), self.r) 
        self.drawSpeed()
        self.drawAcc( ) 
        
        
    # Update cinematis.
    # Speed and position can be overriden by passing a list with new values. If not, they are computed.
    # Acceleration, since is the "most derivated one" only takes new values.
    def updateSpeed( self , new_speed  = None ) :
        
        if new_speed == None :
            self.speed_x = self.speed_x + self.acc_x
            self.speed_y = self.speed_y + self.acc_y       
        else:
            self.speed_x = new_speed[ 0 ]
            self.speed_y = new_speed[ 1 ]
            
    def updateAcc( self , new_acc = None ) :
        
        if new_acc == None:
            print( "No new acceleration!" )
            
        else :
            self.acc_x = new_acc[ 0 ]
            self.acc_y = new_acc[ 1 ]
            
    def updatePos( self , new_pos = None ) :
        
        if new_pos == None :
            self.xc = self.xc + self.speed_x
            self.yc = self.yc + self.speed_y 
        else:
            self.xc = new_pos[ 0 ]
            self.yc = new_pos[ 1 ]
            
    
    def update( self ) :
        
        self.updateSpeed( )
        self.updatePos( )
        
        if self.check_collision :
        
            if ( self.xc + self.speed_x + self.r ) > self.screen.get_width( ) or ( self.xc + self.speed_x - self.r ) <= 0:
                self.speed_x = -self.speed_x
    
            if ( self.yc + self.speed_y + self.r ) > self.screen.get_height() or ( self.yc + self.speed_y - self.r ) <= 0:
                self.speed_y = -self.speed_y
            

        self.draw()
        
        
    def center_to_list( self ) :
        return [ self.xc , self.yc ]