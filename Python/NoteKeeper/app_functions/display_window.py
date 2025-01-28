import tkinter as tk 
from NoteDb import NoteDB


def move_on_click( note_list , current , step , text , date_var , is_doto_flag , tags_var ) :

    current[ 0 ] = current[ 0 ] + step 

    if current[ 0 ] >= len( note_list ) :
        current[ 0 ] = 0 
    elif current[ 0 ] < 0 :
        current[ 0 ] = len( note_list ) - 1 + current[ 0 ]    
    
    note = note_list[ current[ 0 ] ] 

    text.delete( "1.0" , tk.END )
    text.insert( "1.0" , note.text.replace( NoteDB.NEW_LINE_CHAR , "\n" ) )

    date_var.set( note.date )
    is_doto_flag.set( note.is_todo )
    tags_var.set( note.tags )

def display_window( root , note_list ) :

    current = [ 0 ] # Dirty trick to keep the current index of the note displayed. Wrapping an int into a list so it is passed by reference and I can "return" it.
    slave = tk.Toplevel( root )
    
    text_label = tk.Label( slave , text = "Text : " )
    text = tk.Text( slave )
    text.insert( "1.0" , note_list[ 0 ].text.replace( NoteDB.NEW_LINE_CHAR , "\n" ) )

    date_var = tk.StringVar( ) 
    date_label = tk.Label( slave , text = "Date :" )
    date = tk.Entry( slave , textvariable = date_var )
    date_var.set( note_list[ 0 ].date )

    is_todo_flag = tk.IntVar( )
    is_todo = tk.Checkbutton( slave , text = "Is to do!" , variable = is_todo_flag )
    is_todo_flag.set( note_list[ 0 ].is_todo )
    
    tags_var = tk.StringVar( )
    tags_label = tk.Label( slave , text = "Tags :"  ) 
    tags = tk.Entry( slave , textvariable = tags_var ) 
    tags_var.set( note_list[ 0 ].tags )

    left_button = tk.Button( slave , text = "Back" , command = lambda : move_on_click( note_list , current , 1 , text , date_var , is_todo_flag , tags_var ) )
    right_button = tk.Button( slave , text = "Forward" , command = lambda : move_on_click( note_list , current , -1 , text , date_var , is_todo_flag , tags_var ) )

    COL_SLAVE = 0 
    ROW_SLAVE = 0
    text_label.grid( row = ROW_SLAVE , column = COL_SLAVE )
    text.grid( row = ROW_SLAVE , column = COL_SLAVE + 1 ) 
    
    ROW_SLAVE = ROW_SLAVE + 1 
    date_label.grid( row = ROW_SLAVE , column = COL_SLAVE )
    date.grid( row = ROW_SLAVE , column = COL_SLAVE + 1 ) 


    ROW_SLAVE = ROW_SLAVE + 1 
    tags_label.grid( row = ROW_SLAVE , column = COL_SLAVE )
    tags.grid( row = ROW_SLAVE , column = COL_SLAVE + 1 ) 

    ROW_SLAVE = ROW_SLAVE + 1
    is_todo.grid( row = ROW_SLAVE , column = COL_SLAVE ) 

    ROW_SLAVE = ROW_SLAVE + 1
    left_button.grid( row = ROW_SLAVE , column = COL_SLAVE )
    COL_SLAVE = COL_SLAVE + 1  
    right_button.grid( row = ROW_SLAVE , column = COL_SLAVE ) 


    