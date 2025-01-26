import tkinter as tk
import NoteDb as db
from app_functions import *


WIDTH = 200
HEIGHT = 150
STICKY = "ew"
PADX = 0
PADY = 10 
WEIGHT = 1 
COL_SPAN = 4 

root = tk.Tk( )
root.minsize( WIDTH , HEIGHT )
note_db = db.NoteDB( )
note_db.load_settings( "settings.json" )

# Buttons definition
load_button = tk.Button( root , text = "Load database!" , command = lambda : load_on_click( note_db ) )
add_button = tk.Button( root , text = "Add a note!" , command = lambda : add_note_on_click( root , note_db ) ) 
find_button = tk.Button( root , text = "Find a note!" , command = lambda : invoke_find_window( root , note_db ) ) 
save_button = tk.Button( root , text = "Save db!" , command = lambda : note_db.save_db( ) )  
delete_button = tk.Button( root , text = "Delete by ID!" , command = lambda : delete_on_click( root , note_db ) )  
print_unique_tags = tk.Button( root , text = "Print unique tags!" , command = lambda : note_db.print_unique_tags( ) ) 
print_button = tk.Button( root , text = "Print db!" , command = lambda : note_db.print_dict(  ) )
setting_button = tk.Button( root , text = "Change settings!" , command = lambda : change_settings_on_click( root , note_db ) ) 


# Packing into grid
COL = 0
ROW = 0 
load_button.grid( row = ROW , column = COL , sticky = STICKY , padx = PADX , pady = PADY , columnspan = COL_SPAN ) 
root.columnconfigure( ( ROW , COL ) , weight = WEIGHT )

ROW = ROW + 1 
print_button.grid( row = ROW , column = COL , sticky = STICKY , padx = PADX , pady = PADY , columnspan = COL_SPAN ) 
root.columnconfigure( ( ROW , COL ) , weight = WEIGHT )

ROW = ROW + 1 
find_button.grid( row = ROW , column = COL , sticky = STICKY , padx = PADX , pady = PADY , columnspan = COL_SPAN ) 
root.columnconfigure( ( ROW , COL ) , weight = WEIGHT )

ROW = ROW + 1 
add_button.grid( row = ROW , column = COL , sticky = STICKY , padx = PADX , pady = PADY , columnspan = COL_SPAN ) 
root.columnconfigure( ( ROW , COL ) , weight = WEIGHT )

ROW = ROW + 1
print_unique_tags.grid( row = ROW , column = COL , sticky = STICKY , padx = PADX , pady = PADY , columnspan = COL_SPAN ) 
root.columnconfigure( ( ROW , COL ) , weight = WEIGHT )

ROW = ROW + 1
delete_button.grid( row = ROW , column = COL , sticky = STICKY , padx = PADX , pady = PADY , columnspan = COL_SPAN ) 
root.columnconfigure( ( ROW , COL ) , weight = WEIGHT )

ROW = ROW + 1
save_button.grid( row = ROW , column = COL , sticky = STICKY , padx = PADX , pady = PADY , columnspan = COL_SPAN ) 
root.columnconfigure( ( ROW , COL ) , weight = WEIGHT )

ROW = ROW + 1 
print_unique_tags.grid( row = ROW , column = COL , sticky = STICKY , padx = PADX , pady = PADY , columnspan = COL_SPAN )  
root.columnconfigure( ( ROW , COL ) , weight = WEIGHT )

ROW = ROW + 1 
setting_button.grid( row = ROW , column = COL , sticky = STICKY , padx = PADX , pady = PADY , columnspan = COL_SPAN ) 
root.columnconfigure( ( ROW , COL ) , weight = WEIGHT )


root.protocol( "WM_DELETE_WINDOW" , lambda : close_app( root , note_db ) ) 

root.mainloop( )