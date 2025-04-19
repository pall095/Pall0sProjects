import tkinter as tk
from Game import Game
import pygame
from PIL import Image , ImageTk
from windows import define_planet_window
from start_game_function import start_game
import app_data.Configs.app_config as _APP_CONFIG
import app_data.Configs.game_config as _GAME_CONFIG

root = tk.Tk( )
root.geometry( _APP_CONFIG.MAIN_WINDOW_SIZE )
planet_dict_list = list(  )

#Define Image
image = ImageTk.PhotoImage( Image.open( _APP_CONFIG.IMAGE_PATH ).resize( _APP_CONFIG.IMAGE_SIZE ) )
image_label = tk.Label( root , image = image )

# Create planet button
define_planet_button  = tk.Button( root , text = "Define a planet" , command = lambda : define_planet_window.define_planet_window( root ,  planet_dict_list ) ) 

# Load Planets
load_planets_button  = tk.Button( root , text = "Load planets" , command = lambda : define_planet_window.load_planets( planet_dict_list ) ) 

# Start button
start_button = tk.Button( root , text = "Start game" , command = lambda : start_game( planet_dict_list ) )

ROW = 0 
COL = 0 
image_label.grid( row = ROW , column = COL , padx = _APP_CONFIG.PADX , pady = _APP_CONFIG.PADY , sticky = _APP_CONFIG.STICKY )
root.grid_columnconfigure( COL , weight = 2 )

ROW = ROW +1 
define_planet_button.grid( row = ROW , column = COL , padx = _APP_CONFIG.PADX , pady = _APP_CONFIG.PADY , sticky = _APP_CONFIG.STICKY )

ROW = ROW + 1
load_planets_button.grid( row = ROW , column = COL , padx = _APP_CONFIG.PADX , pady = _APP_CONFIG.PADY , sticky = _APP_CONFIG.STICKY )

ROW = ROW + 1
start_button.grid( row = ROW , column = COL , padx = _APP_CONFIG.PADX , pady = _APP_CONFIG.PADY , sticky = _APP_CONFIG.STICKY )

root.mainloop( )