import NoteDb as db
import Note as nt
from tkinter import filedialog
import tkinter as tk 
import datetime

def load_on_click( note_db ) :
    DB_PATH = filedialog.askopenfilename( ) 
    note_db.load_from_file( DB_PATH ) 

def close_app( root , note_db ) :
    if( note_db.autosave == True ) :
        note_db.save_db( )

    root.destroy( )

def save_new_note_on_click( window , note_db , text , date , is_todo_flag , tags ) :
    
    new_note = nt.Note( text = text.get( "1.0" , 'end-1c' ) ,
                       date = date.get( ) ,
                       is_todo = is_todo_flag.get( ) , 
                       tags = tags.get( ).split( db.NoteDB.TAGS_DELIMITER ) )  
    note_db.add_note( new_note ) 
    window.destroy( )

