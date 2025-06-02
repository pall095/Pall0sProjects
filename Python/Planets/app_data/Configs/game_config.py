
GAME_WIDTH = 700
GAME_HEIGHT = 700
SCREEN_DIMENSIONS = ( GAME_WIDTH , GAME_HEIGHT )
GAME_SPEED = 0.01
BG_PATH = r"app_data/Images/bg_image.jpg"

VECTORS_RESCALE_FACTOR = 20
SPEED_VECTOR_RGB = [255 , 0 , 0 ] 
ACC_VECTOR_RGB = [ 0 , 0 , 255 ]

# Behavior
RESET_ON_CLOSURE = True # If true, when terminating a run, need to re-load all the planets.
DRAW_TAIL = True # Allow to draw the tail of planets (i.e. the trajectory ) 
TAIL_RADIUS = 1 # Radius of the tail "circle"
