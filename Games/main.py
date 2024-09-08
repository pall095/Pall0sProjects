# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()
from Circle import Circle
from Game import Game
import time
import random

WIDTH = 700
HEIGHT = 700
RANGE = 200

delay = 0.01
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
initial_pos = [ 100 , 500 ]
initial_speed = [ 1 , 0 ]
initial_acc = [ 0.0 , 0.0 ]


#Planet 1
planet1 = Circle( screen , "Planet 1" , initial_pos , radius , mass ,  [ 255 , 0 , 255 ] , initial_speed , initial_acc , check_collision = False , check_gravity = True )

#Planet 1
planet2 = Circle( screen , "Planet 2" , [ 100 , 100 ], radius , mass*2 ,  [ 0  , 0 , 255 ] , initial_speed , initial_acc , check_collision = False , check_gravity = True )
# Sun
sun = Circle( screen , "Sun" , [ WIDTH/2 , HEIGHT/2 ] , radius/2 , mass*1000 , [ 0 , 0 , 0 ] , check_collision = False , check_gravity = False )
circle_list = [ planet1 , planet2 , sun ]
g = Game( screen , circle_list , delay , verbose = True )
g.start( )