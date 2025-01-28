import tkinter as tk 

def delete_window( root , note_db ) :

    slave = tk.Toplevel( root )
    id_label = tk.Label( slave , text = "Type the ID to remove :" )
    id_entry = tk.Entry( slave )
    delete_button = tk.Button( slave , text = "Delete!" , command = lambda : note_db.delete( int( id_entry.get( ) ) ) )
    close_button = tk.Button( slave , text = "Close" , command = lambda : slave.destroy( ) )

    id_label.grid( row = 0 , column = 0  )
    id_entry.grid( row = 0 , column = 1  )
    delete_button.grid( row = 0 , column = 2 )
    close_button.grid( row = 0 , column = 3 )