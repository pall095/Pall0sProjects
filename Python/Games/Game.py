# Simple pygame program

# Import and initialize the pygame library
import pygame
import sys
from Circle import Circle
import time
import random
from utils import dist, gravityComp, gravityModule
from threading import Thread



class Game :
    
    def __init__( self , screen , object_list , game_speed ) :
        
        self.game_speed = game_speed
        self.screen = screen
        self.object_list = object_list
        self.isRunning = False
        self.thread = None
        
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
                self.computeGravitiy( )
                circle.update( )
            # Flip the display
            pygame.display.flip()
            time.sleep( self.game_speed )
         
        return
        
    def computeGravitiy( self ) :
        
        for p1 in self.object_list :
            
            if p1.check_gravity:
                
                for p2 in self.object_list :
                    
                    tmp_x , tmp_y = gravityComp( p2 , p1 )
                    p1.acc_x = tmp_x
                    p1.acc_y = tmp_y
  
                