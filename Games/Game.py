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
    
    def __init__( self , game_speed , window_size ) :
        
        self.game_speed = game_speed
        self.size = window_size
        self.isRunning = False
        self.thread = None
        
    def __del__( self ) :
        print( "Destructor called!")
        
    def stop( self ) :
        self.isRunning = False
        self.thread.join( )
        print( self.thread.is_alive() )
        return
        #pygame.quit( )

        
    def start( self ) :
        if self.isRunning == False :
            self.isRunning == True 
        
        self.thread = Thread( target = self.game_loop )
        self.thread.setDaemon( True )
        self.thread.start()
        pygame.init()
        print( self.thread.is_alive() )

    def game_loop( self ) :
        
        pygame.init()
        
        
        WIDTH = self.size[ 0 ]
        HEIGHT = self.size[ 1 ]
        RANGE = 200
        
        # Set up the drawing window
        screen = pygame.display.set_mode([ WIDTH , HEIGHT ] )
       
        # Planet
        initial_x = random.randint( WIDTH / 2 - RANGE , WIDTH / 2 + RANGE )
        initial_y = random.randint( HEIGHT / 2 - RANGE , HEIGHT / 2 + RANGE )
        radius = 10
        mass = 1  
        initial_x_speed = 8
        initial_y_speed = 7
        initial_pos = [ initial_x , initial_y ]
        initial_speed = [ initial_x_speed , initial_y_speed ]
        initial_acc = [ 0 , 0 ]
        
        check_wall_collision = False 
        
        
        planet = Circle( screen , 
                    initial_pos ,
                    radius ,
                    mass , 
                    [ 255 , 0 , 255 ] , 
                    initial_speed ,
                    initial_acc )
        
        
        # Sun
        c2 = Circle( screen , [ WIDTH/2 , HEIGHT/2 ] , radius/2 , mass*20000 , [ 0 , 0 , 0 ] , check_collision = True )
        
        # Run until the user asks to quit
        self.isRunning = True
        while self.isRunning:
        
            print( "In game check: " + str( self.thread.is_alive() ) )
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.isRunning == False:
                    pygame.quit()
                    sys.exit( )
                    break
        
            # Fill the background with white
            screen.fill((255, 255, 255))
            
            x_comp , y_comp = gravityComp(c2 , planet )
            planet.acc_x = x_comp * gravityModule( c2 , planet )
            planet.acc_y = y_comp * gravityModule( c2 , planet )
            
        
            # Draw a solid blue circle in the center
            for circle in Circle.circleList :
                circle.update( )
            # Flip the display
            pygame.display.flip()
            time.sleep( self.game_speed )
         
        return
        
            
        
        # Done! Time to quit.
        #self.stop( )