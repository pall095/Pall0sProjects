import pygame



class Circle:
    
    circleList = [ ]
    vectorMultiplier = 2 
    
    def __init__( self , screen , initial_pos : list , r , mass , rgb : list , speed = [ 0, 0 ] , acc = [ 0 , 0 ] , check_collision = False ) :
        
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
        
        self.rgb = rgb
        self.circleList.append( self )
        
        
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
        
        
    def updateSpeed( self ) :
        
        self.speed_x = self.speed_x + self.acc_x
        self.speed_y = self.speed_y + self.acc_y
    
    def update( self ) :
        
        self.updateSpeed()
        
        if self.check_collision :
        
            if ( self.xc + self.speed_x + self.r ) > self.screen.get_width( ) or ( self.xc + self.speed_x - self.r ) <= 0:
                self.speed_x = -self.speed_x
    
            if ( self.yc + self.speed_y + self.r ) > self.screen.get_height() or ( self.yc + self.speed_y - self.r ) <= 0:
                self.speed_y = -self.speed_y
            
        self.xc = self.xc + self.speed_x
        self.yc = self.yc + self.speed_y
        self.draw()