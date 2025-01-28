import tkinter as tk 
# CURRENTLY NOT WORKING CORRECTLY
def setting_window( root , note_db ) :

    slave = tk.Toplevel( root )
    autosave_flag = tk.IntVar( slave , value = note_db.autosave )
    autosave = tk.Checkbutton( slave , text = "Autosave" , variable = autosave_flag , onvalue = 1 , offvalue = 0 ) 
    autofilldate_flag = tk.IntVar( slave , value = note_db.autofill_date )
    autofill = tk.Checkbutton( slave , text = "Autofill date" , variable = autofilldate_flag )

    autosave.grid( row = 0 , column = 0 )
    autofill.grid( row = 0 , column = 1 ) 

