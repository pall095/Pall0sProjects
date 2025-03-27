import tkinter as tk
from tkinter import ttk
import app_header as hdr    
from solve_wrapper import *


root = tk.Tk( )
root.geometry( hdr.WINDOW_SIZE )

solving_method_var = tk.StringVar( )
solving_method_label = tk.Label( root , text = "Select solving ethod" ) 
solving_method_dropdown = ttk.Combobox( root , textvariable = solving_method_var , values = hdr.solving_methods )
solving_method_var.set( hdr.solving_methods[ 0 ] ) 

generation_method_var = tk.StringVar( )
generation_method_label = tk.Label( root , text = "Select generation ethod" ) 
generation_method_dropdown = ttk.Combobox( root , textvariable = generation_method_var , values = hdr.generation_methods )
generation_method_var.set( hdr.generation_methods[ 0 ] ) 

row_var = tk.IntVar( )
row_label = tk.Label( root , text = "Num rows : " ) 
row_entry = tk.Entry( root , textvariable = row_var )
row_var.set( 100 )

col_var = tk.IntVar( )
col_label = tk.Label( root , text = "Num columns : " ) 
col_entry = tk.Entry( root , textvariable = col_var )
col_var.set( 100 )

wall_thr_var = tk.StringVar( )
wall_thr_label = tk.Label( root , text = "Wall Threshold : " ) 
wall_thr_entry = tk.Entry( root , textvariable = wall_thr_var )
wall_thr_var.set( 0.7 )


save_output_var = tk.BooleanVar( )
save_output_label = tk.Label( root , text = "Save output maze" )
save_output_check = tk.Checkbutton( root , variable = save_output_var )

separator_label = tk.Label( root , text = hdr.separator_text )


solve_maze_button = tk.Button( root , text = "Solve maze" , command = lambda : solve_maze( ROW = row_var.get( ) ,
                                                                                           COL = col_var.get( ) ,
                                                                                           generation_method = generation_method_var.get( ) ,
                                                                                           solving_method = solving_method_var.get( ) , 
                                                                                           save_output = save_output_var.get( ) ,  
                                                                                           wall_thr = float( wall_thr_var.get( ) ) ) )

ROW = 0 
COL = 0 
solving_method_label.grid( row = ROW , column = COL , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )
COL = COL + 1 
solving_method_dropdown.grid( row = ROW , column = COL , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )

COL = 0 
ROW = ROW + 1
generation_method_label.grid( row = ROW , column = COL , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )
COL = COL + 1 
generation_method_dropdown.grid( row = ROW , column = COL , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )

ROW = ROW + 1
COL = 0 
separator_label.grid( row = ROW , column = COL , columnspan = 2 , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )

ROW = ROW + 1
COL = 0 
row_label.grid( row = ROW , column = COL , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )
COL = COL + 1
row_entry.grid( row = ROW , column = COL , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )

ROW = ROW + 1
COL = 0 
col_label.grid( row = ROW , column = COL , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )
COL = COL + 1
col_entry.grid( row = ROW , column = COL , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )

ROW = ROW + 1 
COL = 0
wall_thr_label.grid( row = ROW , column = COL , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )
COL = COL + 1
wall_thr_entry.grid( row = ROW , column = COL , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )

ROW = ROW + 1 
COL = 0 
save_output_label.grid( row = ROW , column = COL , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )
COL = COL + 1
save_output_check.grid( row = ROW , column = COL , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )

ROW = ROW + 1
COL = 0 
solve_maze_button.grid( row = ROW , column = COL , columnspan = 2 , sticky = hdr.STICKY , padx = hdr.PADX , pady = hdr.PADY )



root.mainloop( )