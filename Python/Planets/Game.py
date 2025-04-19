# Simple pygame program

# Import and initialize the pygame library
import pygame
import sys
from Circle import Circle
import time
import random
import utils as utl
from threading import Thread
import app_data.Configs.game_config as _GAME_CONFIG



class Game :

    def __init__( self , object_list : list ) :
        
        self.game_speed = _GAME_CONFIG.GAME_SPEED
        self.WIDTH = _GAME_CONFIG.GAME_WIDTH
        self.HEIGHT = _GAME_CONFIG.GAME_WIDTH
        self.screen = None
        self.background = pygame.transform.scale( pygame.image.load( _GAME_CONFIG.BG_PATH ) , ( self.WIDTH , self.HEIGHT ) )
        self.object_list = object_list
        self.isRunning = False
        self.thread = None
        
    def __del__( self ) :
        self.object_list = list( )
        print( "Destructor called! - Resetting object list")
        
        
    def start( self ) :

        if len( self.object_list ) == 0 :
            raise RuntimeError( "Planet list is empty!" )
        else :
            self.game_loop( )

    def game_loop( self ) :
        
        # Run until the user asks to quit
        self.screen = pygame.display.set_mode([ self.WIDTH , self.HEIGHT ] )
        self.isRunning = True
        while self.isRunning :
        
            self.screen.blit( self.background , (0, 0) )
        
            # Draw a solid blue circle in the center
            for circle in self.object_list :
                
                self.compute_gravitiy( )
                circle.update_speed( )
                circle.update_pos( )
                        
                self.check_collision( )             
                self.draw_planet( circle )
            # Flip the display
            pygame.display.flip()
            time.sleep( self.game_speed )

            for event in pygame.event.get() :
                if event.type == pygame.QUIT or self.isRunning == False:
                    self.isRunning = False 
                    pygame.quit()
                    break
         
        return
    

    def add_planet( self , new_circle : Circle ) :
        self.object_list.append( new_circle )
    
    def draw_planet( self , circle : Circle ) :

        # Drawign planet
        pygame.draw.circle( self.screen , circle.rgb , circle.get_current_pos( ) , circle.get_radius( ) )

        # Drawing speed vector
        pygame.draw.line( self.screen , _GAME_CONFIG.SPEED_VECTOR_RGB , circle.get_current_pos( ) , circle.get_speed_vector( _GAME_CONFIG.VECTORS_RESCALE_FACTOR ) )

        # Drawing acceleration vector
        pygame.draw.line( self.screen , _GAME_CONFIG.ACC_VECTOR_RGB , circle.get_current_pos( ) , circle.get_acc_vector( _GAME_CONFIG.VECTORS_RESCALE_FACTOR ) )

    # --- GAME PHYSICS --- #
    def compute_gravitiy( self ) :    
        
        for element in self.object_list :
            if element.check_gravity :            
                acc_x = 0 
                acc_y = 0 
                for element_2 in self.object_list :  
                    if element.name == element_2.name :
                        continue
                    else:
                        tmp_x , tmp_y = utl.calculate_gravity( element , element_2 )
                        acc_x = acc_x + tmp_x 
                        acc_y = acc_y + tmp_y                
                
                element.impose_acc( [acc_x , acc_y ] ) 
                                 
        return 
    

    def check_collision( self ):
        
        for element in self.object_list :
            
            if element.check_collision :
                
                if ( element.xc + element.speed_x + element.r ) > self.screen.get_width( ) or ( element.xc + element.speed_x - element.r ) <= 0:
                    element.impose_speed( [ -element.speed_x , element.speed_y ] )
                    #element.impose_acc( [ -element.acc_x , element.acc_y ] )
        
                if ( element.yc + element.speed_y + element.r ) > self.screen.get_height() or ( element.yc + element.speed_y - element.r ) <= 0:
                    element.impose_speed( [ element.speed_x , -element.speed_y ] )
                    #element.impose_acc( [ element.acc_x, -element.acc_y ] )
  
                