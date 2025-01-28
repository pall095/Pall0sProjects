import tkinter as tk 

def get_selected_tags( tag_list ) :

    selected = list( )
    for i in tag_list.curselection( ) :
        selected.append( tag_list.get( i ) )

    if not selected :
        return "any"
    else :
        return selected

def find_window( root , note_db ) :

    found_list = list( )

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

    is_todo_flag = tk.IntVar( slave )
    is_todo = tk.Checkbutton( slave , text = "Is to do!" , variable = is_todo_flag )

    date_text = tk.StringVar( slave , value = DEFAULT )
    date_label = tk.Label( slave , text = "Date :")
    date_entry = tk.Entry( slave , textvariable = date_text )
    

    find_button = tk.Button( slave , text = "Find" , command = lambda : note_db.find( found_list ,
                                                                                      content = keyword_text.get( ) , 
                                                                                      tags = get_selected_tags( tag_list ) ,
                                                                                      is_todo = int( is_todo_flag.get( ) ) ,
                                                                                      date = date_text.get( ) ) ) 

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
    is_todo.grid( row = ROW , column = COL ) 

    ROW = ROW + 1
    COL = 0 
    find_button.grid( row = ROW , column = COL )
