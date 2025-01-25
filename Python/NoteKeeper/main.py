import Note as nt
import NoteDb as DB


db = DB.NoteDB(  ) 
db.load_from_file( "note_db.txt" )

COMMAND = 0 

while COMMAND != -1 :
    
    
    print( "What do you want to do: " )
    print( "0 : print db" )
    print( "1 : add new note" )
    print( "2 : save db" )
    print( "3 : delete" )
    print( "4 : print unique tags" )
    print( "5 : reaload db" )
    print( "-1 : terminate" )
    
    COMMAND = int( input( "Type your command: ") )

    if COMMAND == -1 :
        continue 

    elif COMMAND == 0 :
        db.print_dict( ) 
    
    elif COMMAND == 1 :    
        text = input( "Add note content: " ) 
        date = input( "Add date:" )
        is_meeting = input( "Is meeting flag: " )
        is_todo = input( "Is todo flag: " )
        deadline = input( "Add deadline:" ) 
        tags = input( "Add tags (separated by comma:) " ) 
        tags = tags.split( "," ) 

        note = nt.Note( text , date  , is_meeting , is_todo , deadline , tags )
        db.add_note( note )  

    elif COMMAND == 2 :
        db.save_db( )

    elif COMMAND == 3 :
        id_del = int( input( "Insert the ID to delete: ") ) 
        db.delete( id_del ) 

    elif COMMAND == 4 :
        db.print_unique_tags( )

    elif COMMAND == 5 :
        db.load_from_file( "note_db.txt" )


    else :
        print( "Invalid command!" ) 

