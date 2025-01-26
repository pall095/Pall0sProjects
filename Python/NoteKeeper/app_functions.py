import NoteDb as db
import Note as nt
from tkinter import filedialog
import tkinter as tk 
import datetime

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

    if note_db.autofill_date :
        date.insert( 0 , datetime.datetime.strftime( datetime.date.today() , format = "%d-%m-%Y" ) )

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


# CURRENTLY NOT WORKING CORRECTLY
def change_settings_on_click( root , note_db ) :

    slave = tk.Toplevel( root )
    autosave_flag = tk.IntVar( slave , value = note_db.autosave )
    autosave = tk.Checkbutton( slave , text = "Autosave" , variable = autosave_flag , onvalue = 1 , offvalue = 0 ) 
    autofilldate_flag = tk.IntVar( slave , value = note_db.autofill_date )
    autofill = tk.Checkbutton( slave , text = "Autofill date" , variable = autofilldate_flag )

    autosave.grid( row = 0 , column = 0 )
    autofill.grid( row = 0 , column = 1 ) 


def close_app( root , note_db ) :

    if( note_db.autosave == True ) :
        note_db.save_db( )

    root.destroy( )


def delete_on_click( root , note_db ) :

    slave = tk.Toplevel( root )
    id_label = tk.Label( slave , text = "Type the ID to remove :" )
    id_entry = tk.Entry( slave )
    delete_button = tk.Button( slave , text = "Delete!" , command = lambda : note_db.delete( int( id_entry.get( ) ) ) )
    close_button = tk.Button( slave , text = "Close" , command = lambda : slave.destroy( ) )

    id_label.grid( row = 0 , column = 0  )
    id_entry.grid( row = 0 , column = 1  )
    delete_button.grid( row = 0 , column = 2 )
    close_button.grid( row = 0 , column = 3 )

def get_selected_tags( tag_list ) :

    selected = list( )
    for i in tag_list.curselection( ) :
        selected.append( tag_list.get( i ) )

    if not selected :
        return "any"
    else :
        return selected

def invoke_find_window( root , note_db ) :

    DEFAULT = "any"
    slave = tk.Toplevel( root ) 
    slave.minsize( 200 , 200 )

    keyword_text = tk.StringVar( value = DEFAULT )
    keyword_label = tk.Label( slave , text = "Type content :" )
    keyword_entry = tk.Entry( slave , textvariable = keyword_text )

    tags_label = tk.Label( slave , text = "Select Tags : " ) 
    tag_list = tk.Listbox( slave , selectmode = "multiple" )
    for tag in note_db.unique_tags :
        tag_list.insert( tk.END , tag )

    is_meeting_flag = tk.IntVar( slave )
    is_meeting = tk.Checkbutton( slave , text = "Is meeting flag!" , variable = is_meeting_flag ) 
    is_todo_flag = tk.IntVar( slave )
    is_todo = tk.Checkbutton( slave , text = "Is to do!" , variable = is_todo_flag )

    date_text = tk.StringVar( slave , value = DEFAULT )
    date_label = tk.Label( slave , text = "Date :")
    date_entry = tk.Entry( slave , textvariable = date_text )
    
    deadline_text = tk.StringVar( slave , value = DEFAULT )
    deadline_label = tk.Label( slave , text = "Deadline :"  )
    deadline_entry = tk.Entry( slave , textvariable = deadline_text )

    find_button = tk.Button( slave , text = "Find" , command = lambda : note_db.find( content = keyword_text.get( ) , 
                                                                                      tags = get_selected_tags( tag_list ) , 
                                                                                      is_meeting = int( is_meeting_flag.get( ) ) ,
                                                                                      is_todo = int( is_todo_flag.get( ) ) ,
                                                                                      date = date_text.get( ) ,
                                                                                      deadline = deadline_text.get( ) ) ) 


    ROW = 0 
    COL = 0
    keyword_label.grid( row = ROW , column = COL )
    COL = COL + 1 
    keyword_entry.grid( row = ROW , column = COL )

    ROW = ROW + 1
    COL = 0 
    tags_label.grid( row = ROW , column = COL ) 
    COL = COL + 1 
    tag_list.grid( row = ROW , column = COL )

    ROW = ROW + 1
    COL = 0 
    date_label.grid( row = ROW , column = COL ) 
    COL = COL + 1 
    date_entry.grid( row = ROW , column = COL )

    ROW = ROW + 1
    COL = 0 
    deadline_label.grid( row = ROW , column = COL ) 
    COL = COL + 1 
    deadline_entry.grid( row = ROW , column = COL )

    ROW = ROW + 1 
    COL = 0 
    is_meeting.grid( row = ROW , column = COL )
    COL = COL + 1 
    is_todo.grid( row = ROW , column = COL )

    ROW = ROW + 1
    COL = 0 
    find_button.grid( row = ROW , column = COL )