# Simple pygame program

# Import and initialize the pygame library
import pygame
import sys
from Circle import Circle
import time
import random
import utils as utl
from tkinter import filedialog
import json
import app_data.Configs.game_config as _GAME_CONFIG




class Game :

    def __init__( self : list ) :
        
        self.game_speed = _GAME_CONFIG.GAME_SPEED
        self.WIDTH = _GAME_CONFIG.GAME_WIDTH
        self.HEIGHT = _GAME_CONFIG.GAME_HEIGHT
        self.screen = None
        self.bg_image = pygame.image.load( _GAME_CONFIG.BG_PATH )
        self.background = pygame.transform.scale( self.bg_image , ( self.WIDTH , self.HEIGHT ) )
        self.object_list = list( )
        
        self.is_running = False
        self.is_initialized = False
        self.draw_tail_setting = _GAME_CONFIG.DRAW_TAIL
        self.tail_radius_setting = _GAME_CONFIG.TAIL_RADIUS
        self.rest_on_closure_setting = _GAME_CONFIG.RESET_ON_CLOSURE
        
        
    def start( self ) :

        if not( self.is_initialized ) :     
            raise RuntimeError( "Game is not initialized!")
        else :
            self.game_loop( )

    def handle_closure( self ) :

        self.is_running = False 
        
        if self.rest_on_closure_setting :
            print( "Reset setting ON. Re-initialize for next run!" )
            self.is_initialized = False 
            self.object_list = list( )
        else :
            print( "Reset setting OFF. No need to re-initialize at next run!" )

        pygame.quit( )
        return 

    def game_loop( self ) :
        
        # Run until the user asks to quit
        self.screen = pygame.display.set_mode([ self.WIDTH , self.HEIGHT ] , pygame.RESIZABLE )
        self.is_running = True

        while self.is_running :
        
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
                if event.type == pygame.QUIT or self.is_running == False:
                    self.handle_closure( )
                    break
         
        return
    

    def ask_for_planet_files( self ) -> list :

        filenames = filedialog.askopenfilenames( ) 
        planet_dict_list = list( )

        for filename in filenames :
            with open( filename , "r" ) as file :
                data = json.load( file ) 
                planet_dict_list.append( data )

        return planet_dict_list

    def load_from_list( self ) :

        planet_dict_list = self.ask_for_planet_files( )

        for planet_dict in planet_dict_list :   
            circle = Circle.init_from_dict( planet_dict )
            circle.offset_pos( ( _GAME_CONFIG.GAME_WIDTH / 2 , _GAME_CONFIG.GAME_HEIGHT / 2 ) )
            self.object_list.append( circle )

        self.is_initialized = True 


    def add_planet( self , new_circle : Circle ) :
        self.object_list.append( new_circle )
    
    def draw_planet( self , circle : Circle ) :
        # Drawign planet
        pygame.draw.circle( self.screen , circle.rgb , circle.get_current_pos( ) , circle.get_radius( ) )

        # Drawing speed vector
        pygame.draw.line( self.screen , _GAME_CONFIG.SPEED_VECTOR_RGB , circle.get_current_pos( ) , circle.get_speed_vector( _GAME_CONFIG.VECTORS_RESCALE_FACTOR ) )

        # Drawing acceleration vector
        pygame.draw.line( self.screen , _GAME_CONFIG.ACC_VECTOR_RGB , circle.get_current_pos( ) , circle.get_acc_vector( _GAME_CONFIG.VECTORS_RESCALE_FACTOR ) )
        
        if self.draw_tail_setting :
            for point in circle.trajectory_list :
                pygame.draw.circle( self.screen , circle.rgb , point , self.tail_radius_setting )

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
  
                