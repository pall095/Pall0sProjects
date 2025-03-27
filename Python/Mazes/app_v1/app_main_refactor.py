import tkinter as tk
from tkinter import ttk
import app_config_refactor as _APPCONFIG    
from solve_wrapper_refactor import *


root = tk.Tk( )
root.geometry( _APPCONFIG.WINDOW_SIZE )

solving_method_var = tk.StringVar( )
solving_method_label = tk.Label( root , text = "Select solving ethod" ) 
solving_method_dropdown = ttk.Combobox( root , textvariable = solving_method_var , values = _APPCONFIG.SOLVING_METHODS )
solving_method_var.set( _APPCONFIG.SOLVING_METHODS[ 0 ] ) 

generation_method_var = tk.StringVar( )
generation_method_label = tk.Label( root , text = "Select generation ethod" ) 
generation_method_dropdown = ttk.Combobox( root , textvariable = generation_method_var , values = _APPCONFIG.GENERATION_METHODS )
generation_method_var.set( _APPCONFIG.GENERATION_METHODS[ 0 ] ) 

row_var = tk.IntVar( )
row_label = tk.Label( root , text = "Num rows : " ) 
row_entry = tk.Entry( root , textvariable = row_var )
row_var.set( _APPCONFIG.DEFAULT_ROW )

col_var = tk.IntVar( )
col_label = tk.Label( root , text = "Num columns : " ) 
col_entry = tk.Entry( root , textvariable = col_var )
col_var.set( _APPCONFIG.DEFAULT_COL)

cell_size_var = tk.IntVar( )
cell_size_label = tk.Label( root , text = "Cell Size : " ) 
cell_size_entry = tk.Entry( root , textvariable = cell_size_var )
cell_size_var.set( _APPCONFIG.DEFAULT_CELL_SIZE )

wall_thr_var = tk.StringVar( )
wall_thr_label = tk.Label( root , text = "Wall Threshold : " ) 
wall_thr_entry = tk.Entry( root , textvariable = wall_thr_var )
wall_thr_var.set( _APPCONFIG.DEFAULT_WALL_THR )


save_output_var = tk.BooleanVar( )
save_output_label = tk.Label( root , text = "Save output maze" )
save_output_check = tk.Checkbutton( root , variable = save_output_var )

separator_label = tk.Label( root , text = _APPCONFIG.separator_text )


solve_maze_button = tk.Button( root , text = "Solve maze" , command = lambda : solve_maze( ROW = row_var.get( ) ,
                                                                                           COL = col_var.get( ) ,
                                                                                           CELL_SIZE = cell_size_var.get( ) , 
                                                                                           generation_method = generation_method_var.get( ) ,
                                                                                           solving_method = solving_method_var.get( ) , 
                                                                                           save_output = save_output_var.get( ) ,  
                                                                                           wall_thr = float( wall_thr_var.get( ) ) ) )

ROW = 0 
COL = 0 
solving_method_label.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )
COL = COL + 1 
solving_method_dropdown.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )

COL = 0 
ROW = ROW + 1
generation_method_label.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )
COL = COL + 1 
generation_method_dropdown.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )

ROW = ROW + 1
COL = 0 
separator_label.grid( row = ROW , column = COL , columnspan = 2 , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )

ROW = ROW + 1
COL = 0 
row_label.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )
COL = COL + 1
row_entry.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )

ROW = ROW + 1
COL = 0 
col_label.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )
COL = COL + 1
col_entry.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )

ROW = ROW + 1
COL = 0 
cell_size_label.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )
COL = COL + 1
cell_size_entry.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )

ROW = ROW + 1 
COL = 0
wall_thr_label.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )
COL = COL + 1
wall_thr_entry.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )

ROW = ROW + 1 
COL = 0 
save_output_label.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )
COL = COL + 1
save_output_check.grid( row = ROW , column = COL , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )

ROW = ROW + 1
COL = 0 
solve_maze_button.grid( row = ROW , column = COL , columnspan = 2 , sticky = _APPCONFIG.STICKY , padx = _APPCONFIG.PADX , pady = _APPCONFIG.PADY )

root.mainloop( )