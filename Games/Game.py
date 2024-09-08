# Simple pygame program

# Import and initialize the pygame library
import pygame
import sys
from Circle import Circle
import time
import random
import utils as utl
from threading import Thread



class Game :
    
    def __init__( self , screen , object_list , game_speed , verbose = False) :
        
        self.game_speed = game_speed
        self.screen = screen
        self.object_list = object_list
        self.isRunning = False
        self.thread = None
        self.verbose = verbose
        
    def __del__( self ) :
        print( "Destructor called!")
        
    def stop( self ) :
        self.isRunning = False
        #self.thread.join( )
        #print( self.thread.is_alive() )
        return
        #pygame.quit( )
        
    def start( self ) :
        self.game_loop()

    def game_loop( self ) :
        
        pygame.init()
        

        # Run until the user asks to quit
        self.isRunning = True
        while self.isRunning:
            
            self.screen.fill((255, 255, 255)) 
        
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.isRunning == False:
                    pygame.quit()
                    sys.exit( )
                    break
                
            #x_comp , y_comp = gravityComp(c2 , planet )

        
            # Draw a solid blue circle in the center
            for circle in self.object_list :
                
                self.compute_gravitiy( )
                circle.update_speed( )
                circle.update_pos( )
                        
                self.check_collision( )             
                circle.draw( rescale_factor = 1 , verbose = self.verbose )
            # Flip the display
            pygame.display.flip()
            time.sleep( self.game_speed )
         
        return
    
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
                        if self.verbose :                        
                            print( f"Acc X : {acc_x}" )
                            print( f"Acc Y : {acc_y}" )
                            print( f"Computing gravity for: {element.name} aganinst {element_2.name} ")
                
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
  
                