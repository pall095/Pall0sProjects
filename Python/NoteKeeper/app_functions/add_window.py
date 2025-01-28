
import tkinter as tk 
import datetime 
from app_functions.general_function import save_new_note_on_click

def add_window( root , note_db ) :

    slave = tk.Toplevel( root )
    
    text_label = tk.Label( slave , text = "Text : " )
    text = tk.Text( slave  , yscrollcommand = True )

    date_label = tk.Label( slave , text = "Date :" )
    date = tk.Entry( slave )

    if note_db.autofill_date :
        date.insert( 0 , datetime.datetime.strftime( datetime.date.today() , format = "%d-%m-%Y" ) )

    is_todo_flag = tk.IntVar( )
    is_todo = tk.Checkbutton( slave , text = "Is to do!" , variable = is_todo_flag )
    
    
    tags_label = tk.Label( slave , text = "Tags :" )
    tags = tk.Entry( slave ) 

    save_button = tk.Button( slave , text = "Save!" , command = lambda : save_new_note_on_click( window = slave ,
                                                                                                note_db = note_db ,
                                                                                                text = text ,
                                                                                                date = date ,
                                                                                                is_todo_flag = is_todo_flag ,
                                                                                                tags = tags )
                                                                                                ) 

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
    save_button.grid( row = ROW_SLAVE , column = COL_SLAVE )
    slave.title( "New note window!" ) 
