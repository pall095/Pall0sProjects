import pygame
pygame.init()
from Circle import Circle
from Game import Game
import app_data.Configs.game_config as _GAME_CONFIG
import time
import random


def start_game( planet_dict_list : list ) :
    # Set up the drawing window
    planet_list = list( )
    for planet_dict in planet_dict_list :
        circle = Circle.init_from_dict( planet_dict )
        circle.offset_pos( ( _GAME_CONFIG.GAME_WIDTH / 2 , _GAME_CONFIG.GAME_HEIGHT / 2 ) )
        planet_list.append( circle )
        
    g = Game(  planet_list )
    g.start( )