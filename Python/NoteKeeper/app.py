import tkinter as tk
import NoteDb as db
from app_functions import *

root = tk.Tk( )
note_db = db.NoteDB( )

# Buttons definition
load_button = tk.Button( root , text = "Load database!" , command = lambda : load_on_click( note_db ) )
add_button = tk.Button( root , text = "Add a note!" , command = lambda : add_note_on_click( root , note_db ) ) 
save_button = tk.Button( root , text = "Save db!" , command = lambda : note_db.save_db( ) )  
delete_button = tk.Button( root , text = "Delete by ID!" ) 
print_unique_tags = tk.Button( root , text = "Print unique tags!" , command = lambda : note_db.print_unique_tags( ) ) 
print_button = tk.Button( root , text = "Print db!" , command = lambda : note_db.print_dict(  ) )


# Packing into grid
COL = 0
ROW = 0 
load_button.grid( row = ROW , column = COL )

ROW = ROW + 1 
print_button.grid( row = ROW , column = COL )

ROW = ROW + 1 
add_button.grid( row = ROW , column = COL )

ROW = ROW + 1
print_unique_tags.grid( row = ROW , column = COL )

ROW = ROW + 1
delete_button.grid( row = ROW , column = COL )

ROW = ROW + 1
save_button.grid( row = ROW , column = COL )

ROW = ROW + 1 
print_unique_tags.grid( row = ROW , column = COL )

root.mainloop( )