import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog
import json
from Circle import *
import planet_schema as _PLANET_CONFIG

def add_from_gui( planet_dict_list , name_var , rgb_var , mass_var , radius_var ,  pos_x_var , pos_y_var , speed_x_var , speed_y_var , acc_x_var , acc_y_var , collision_flag_var , gravity_flag_var ) :

    data = {
        _PLANET_CONFIG.NAME_KEY: name_var.get( ) ,
        _PLANET_CONFIG.RGB_KEY : rgb_var.get( ) ,
        _PLANET_CONFIG.MASS_KEY : mass_var.get( ) ,
        _PLANET_CONFIG.RADIUS_KEY : radius_var.get( ) ,
        _PLANET_CONFIG.INITIAL_POS_X_KEY : pos_x_var.get( ) ,
        _PLANET_CONFIG.INITIAL_POS_Y_KEY : pos_y_var.get( ) ,
        _PLANET_CONFIG.INITIAL_SPEED_X_KEY : speed_x_var.get( ) ,
        _PLANET_CONFIG.INITIAL_SPEED_Y_KEY : speed_y_var.get( ) ,
        _PLANET_CONFIG.INITIAL_ACC_X_KEY : acc_x_var.get( ) ,
        _PLANET_CONFIG.INITIAL_ACC_Y_KEY : acc_y_var.get( ) ,
        _PLANET_CONFIG.CHECK_COLLISION_KEY : collision_flag_var.get( ) ,
        _PLANET_CONFIG.CHECK_GRAVITY_KEY : gravity_flag_var.get( ) 
    }

    planet_dict_list.append( data )


def save( name_var , rgb_var , mass_var , radius_var , pos_x_var , pos_y_var , speed_x_var , speed_y_var , acc_x_var , acc_y_var , collision_flag_var , gravity_flag_var ) :

    data = {
        _PLANET_CONFIG.NAME_KEY: name_var.get( ) ,
        _PLANET_CONFIG.MASS_KEY: mass_var.get( ) ,
        _PLANET_CONFIG.RADIUS_KEY : radius_var.get( ) ,
        _PLANET_CONFIG.RGB_KEY : rgb_var.get( ) ,
        _PLANET_CONFIG.INITIAL_POS_X_KEY: pos_x_var.get( ) ,
        _PLANET_CONFIG.INITIAL_POS_Y_KEY: pos_y_var.get( ) ,
        _PLANET_CONFIG.INITIAL_SPEED_X_KEY: speed_x_var.get( ) ,
        _PLANET_CONFIG.INITIAL_SPEED_Y_KEY: speed_y_var.get( ) ,
        _PLANET_CONFIG.INITIAL_ACC_X_KEY: acc_x_var.get( ) ,
        _PLANET_CONFIG.INITIAL_ACC_Y_KEY: acc_y_var.get( ) ,
        _PLANET_CONFIG.CHECK_COLLISION_KEY: collision_flag_var.get( ) ,
        _PLANET_CONFIG.CHECK_GRAVITY_KEY: gravity_flag_var.get( ) 
    }

    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")] )
    with open( filename , "w" ) as output_json :
        json.dump( data , output_json , indent = 4 )


def load_to_edit( name_var , rgb_var , mass_var , radius_var ,  pos_x_var , pos_y_var , speed_x_var , speed_y_var , acc_x_var , acc_y_var , collision_flag_var , gravity_flag_var ) :

    filename = filedialog.askopenfile( mode = "r" )
    data = json.load( filename )
    name_var.set( data[ _PLANET_CONFIG.NAME_KEY ] )
    mass_var.set( data[ _PLANET_CONFIG.MASS_KEY ] )
    radius_var.set( data[ _PLANET_CONFIG.RADIUS_KEY ] )
    rgb_var.set( data[ _PLANET_CONFIG.RGB_KEY ] )
    pos_x_var.set( data[ _PLANET_CONFIG.INITIAL_POS_X_KEY ] ) 
    pos_y_var.set( data[ _PLANET_CONFIG.INITIAL_POS_Y_KEY ] )
    speed_x_var.set( data[ _PLANET_CONFIG.INITIAL_SPEED_X_KEY ] )
    speed_y_var.set( data[ _PLANET_CONFIG.INITIAL_SPEED_Y_KEY ] )
    acc_x_var.set( data[ _PLANET_CONFIG.INITIAL_ACC_X_KEY ] )
    acc_y_var.set( data[ _PLANET_CONFIG.INITIAL_ACC_Y_KEY ] )
    collision_flag_var.set( data[ _PLANET_CONFIG.CHECK_COLLISION_KEY ] )
    gravity_flag_var.set( data[ _PLANET_CONFIG.CHECK_GRAVITY_KEY] )


def load_planets( planet_dict_list  ) :

    filenames = filedialog.askopenfilenames( ) 

    for filename in filenames :
        with open( filename , "r" ) as file :
            data = json.load( file ) 
            planet_dict_list.append( data )
            print( f"Adding : { data[ _PLANET_CONFIG.NAME_KEY ] }" )
    


def define_planet_window( root , planet_dict_list ) :

    window = tk.Toplevel( root ) 
    name_var = tk.StringVar( )
    rgb_var = tk.StringVar( )
    mass_var = tk.DoubleVar( )
    radius_var = tk.DoubleVar( )
    pos_x_var = tk.DoubleVar( ) 
    pos_y_var = tk.DoubleVar( )
    speed_x_var = tk.DoubleVar( )
    speed_y_var = tk.DoubleVar( )
    acc_x_var = tk.DoubleVar( )
    acc_y_var = tk.DoubleVar( )
    collision_var = tk.BooleanVar( )
    gravity_var = tk.BooleanVar( )

    fields = [
    ( "Name", name_var ) ,
    ( "Mass", mass_var ) ,
    ( "Radius" , radius_var ) ,
    ( "RGB [R:G:B]" , rgb_var ) ,
    ("Initial Pos X", pos_x_var ),
    ("Initial Pos Y", pos_y_var ),
    ("Initial Speed X", speed_x_var ),
    ("Initial Speed Y", speed_y_var ),
    ("Initial Acc X", acc_x_var ),
    ("Initial Acc Y", acc_y_var ),
    ]

    ROW = 0 
    COL = 0 

    for label_text, var in fields:
        tk.Label( window , text = label_text ).grid( row = ROW , column = COL )
        COL = COL + 1
        tk.Entry( window , textvariable = var ).grid( row = ROW , column = COL )
        ROW = ROW + 1
        COL = 0 

    # Checkboxes
    ROW = ROW + 1
    tk.Label( window , text= "Check collision" ).grid( row = ROW , column = COL )
    COL = COL + 1
    tk.Checkbutton( window , variable=collision_var).grid( row = ROW , column = COL )

    ROW = ROW + 1
    COL = 0 
    tk.Label( window , text= "Check gravity" ).grid( row = ROW , column = COL )
    COL = COL + 1
    tk.Checkbutton( window , variable = gravity_var).grid( row = ROW , column = COL )

    # Save to to json button
    ROW = ROW + 1
    tk.Button( window , text = "Save to json" , command = lambda : save( name_var = name_var , 
                                                                        mass_var = mass_var ,
                                                                        radius_var = radius_var ,
                                                                        rgb_var = rgb_var ,
                                                                        pos_x_var = pos_x_var ,
                                                                        pos_y_var = pos_y_var ,
                                                                        speed_x_var = speed_x_var ,
                                                                        speed_y_var = speed_y_var ,
                                                                        acc_x_var = acc_x_var ,
                                                                        acc_y_var = acc_y_var ,
                                                                        collision_flag_var = collision_var ,
                                                                        gravity_flag_var = gravity_var ) ).grid( row = ROW , column = COL )
    
    ROW = ROW + 1 
    tk.Button( window , text = "Load to edit from json" , command = lambda : load_to_edit(  name_var = name_var , 
                                                                            mass_var = mass_var ,
                                                                            radius_var = radius_var ,
                                                                            rgb_var = rgb_var ,
                                                                            pos_x_var = pos_x_var ,
                                                                            pos_y_var = pos_y_var ,
                                                                            speed_x_var = speed_x_var ,
                                                                            speed_y_var = speed_y_var ,
                                                                            acc_x_var = acc_x_var ,
                                                                            acc_y_var = acc_y_var ,
                                                                            collision_flag_var = collision_var ,
                                                                            gravity_flag_var = gravity_var ) ).grid( row = ROW , column = COL )

    ROW = ROW + 1 
    tk.Button( window , text = "Load to GIU to game" , command = lambda : add_from_gui(  planet_dict_list = planet_dict_list , 
                                                                        name_var = name_var , 
                                                                        mass_var = mass_var ,
                                                                        radius_var = radius_var ,
                                                                        rgb_var = rgb_var ,
                                                                        pos_x_var = pos_x_var ,
                                                                        pos_y_var = pos_y_var ,
                                                                        speed_x_var = speed_x_var ,
                                                                        speed_y_var = speed_y_var ,
                                                                        acc_x_var = acc_x_var ,
                                                                        acc_y_var = acc_y_var ,
                                                                        collision_flag_var = collision_var ,
                                                                        gravity_flag_var = gravity_var ) ).grid( row = ROW , column = COL )

