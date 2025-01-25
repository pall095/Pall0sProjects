import NoteDb as db
import Note as nt
from tkinter import filedialog
import tkinter as tk 

def load_on_click( note_db ) :

    DB_PATH = filedialog.askopenfilename( ) 
    note_db.load_from_file( DB_PATH ) 

def save_new_note_on_click( window , note_db , text , date , is_meeting_flag , is_todo_flag , deadline , tags ) :
    
    new_note = nt.Note( text = text.get( "1.0" , 'end-1c' ) ,
                       date = date.get( ) ,
                       is_meeting = is_meeting_flag.get( ) ,
                       is_todo = is_todo_flag.get( ) , 
                       deadline = deadline.get( ) ,
                       tags = tags.get( ).split( db.NoteDB.TAGS_DELIMITER ) )  
    note_db.add_note( new_note ) 
    window.destroy( )

    
def add_note_on_click( root , note_db ) :

    slave = tk.Toplevel( root )
    
    text_label = tk.Label( slave , text = "Text : " )
    text = tk.Text( slave  , yscrollcommand = True )

    date_label = tk.Label( slave , text = "Date :" )
    date = tk.Entry( slave )

    is_meeting_flag = tk.IntVar( ) 
    is_meeting = tk.Checkbutton( slave , text = "Is meeting flag!" , variable = is_meeting_flag ) 
    is_todo_flag = tk.IntVar( )
    is_todo = tk.Checkbutton( slave , text = "Is to do!" , variable = is_todo_flag )
    
    deadline_label = tk.Label( slave , text = "Deadline :")
    deadline = tk.Entry( slave )
    
    tags_label = tk.Label( slave , text = "Tags :" )
    tags = tk.Entry( slave ) 

    save_button = tk.Button( slave , text = "Save!" , command = lambda : save_new_note_on_click( window = slave ,
                                                                                                note_db = note_db ,
                                                                                                text = text ,
                                                                                                date = date ,
                                                                                                is_meeting_flag = is_meeting_flag ,
                                                                                                is_todo_flag = is_todo_flag ,
                                                                                                deadline = deadline ,
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
    deadline_label.grid( row = ROW_SLAVE , column = COL_SLAVE )
    deadline.grid( row = ROW_SLAVE , column = COL_SLAVE + 1 ) 

    ROW_SLAVE = ROW_SLAVE + 1 
    tags_label.grid( row = ROW_SLAVE , column = COL_SLAVE )
    tags.grid( row = ROW_SLAVE , column = COL_SLAVE + 1 ) 

    COL_SLAVE = COL_SLAVE + 3
    ROW_SLAVE = 0  
    is_meeting.grid( row = ROW_SLAVE , column = COL_SLAVE ) 

    ROW_SLAVE = ROW_SLAVE + 1
    is_todo.grid( row = ROW_SLAVE , column = COL_SLAVE ) 
    
    
    ROW_SLAVE = ROW_SLAVE + 1
    save_button.grid( row = ROW_SLAVE , column = COL_SLAVE )
    slave.title( "New note window!" ) 
