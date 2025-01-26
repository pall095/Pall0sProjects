import Note as nt
import json 
import Logger as lg

class NoteDB :

    DELIMITER = "|"
    TAGS_DELIMITER = ","
    NEW_LINE_CHAR = "#"
    AUTOLOAD_KEY = "autoload"
    AUTOLOAD_PATH_KEY = "autoload_path"
    AUTOSAVE_KEY = "autosave" 
    AUTOFILL_DATE_KEY = "autofill_date"

    def __init__( self ) :
        
        self.db_path = ""
        self.settings_path = ""
        self.db_len = 0 
        self.db_dict = dict( )
        self.unique_tags = list( )
        
        self.logger = lg.Logger( )
        self.autoload = False 
        self.is_initialzied = False 
        self.autosave = False
        self.autofill_date = False


    def add_note( self , note : nt.Note ) :
        note.text = note.text.replace( "\n" , self.NEW_LINE_CHAR )
        self.update_unique( note.tags )
        self.db_len = self.db_len + 1 
        self.db_dict[ self.db_len ] = note 
        

    def load_settings( self , path = "" ) :
        self.settings_path = path 
        with open( path ) as settings_file :
            settings = json.load( settings_file ) 
            self.autoload = settings[ self.AUTOLOAD_KEY ] 
            self.autosave = settings[ self.AUTOSAVE_KEY ] 
            self.autofill_date = settings[ self.AUTOFILL_DATE_KEY ] 

            if self.autoload :
                self.load_from_file( settings[ self.AUTOLOAD_PATH_KEY ] ) 


    def load_from_file( self , path = "") :
        
        self.logger.print_info( "Initializing db!" )
        self.is_initialzied = True
        self.db_path = path 
        with open( self.db_path ) as db_file :
            for line in db_file :
                self.db_len = self.db_len + 1
                line = line.rstrip( )
                text , date , is_meeting , is_todo , deadline , tags = line.split( self.DELIMITER ) 
                tags = tags.split( self.TAGS_DELIMITER )
                self.update_unique( tags ) 
                self.db_dict[ self.db_len ] = nt.Note( text , date , is_meeting , is_todo , deadline , tags )

    # deletes an object by ID and re-generates the list of unique tags.
    def delete( self , id ) :
        self.logger.print_info( f"Deleting { id }")
        self.db_dict.pop( id ) 
        self.db_len = self.db_len - 1 
        self.regenerate_unique_tags( )

    # Updates the list of unique tags given a new 
    def update_unique( self , new_tags ) :
        for t in new_tags :
            if t not in self.unique_tags :
                self.unique_tags.append( t ) 

    def regenerate_unique_tags( self ) :
        self.unique_tags = list( )

        for key in self.db_dict.keys( ) :
            note = self.db_dict[ key ] 
            tags = note.tags 
            for t in tags :
                if t not in self.unique_tags :
                    self.unique_tags.append( t )

    # Reformats a note object to the correct format to dump in the database.
    def reformat_note( self , note ) :
        list_note = note.to_list( ) 
        s = ""
        for field in list_note :
            # Handles tag by checking if the current field is a list.
            if type( field ) != list :
                s = s + str( field ) + self.DELIMITER 
            else :
                for tag in field :
                    s = s + tag + self.TAGS_DELIMITER 
        s = s.rstrip( self.TAGS_DELIMITER )
        s = s.replace( "\n" , self.NEW_LINE_CHAR )
        return s + "\n"
         
    def save_db( self ) :

        if self.is_initialzied :
            self.logger.print_info( "Saving db!")
            with open( self.db_path , "w" ) as file :
                for key in self.db_dict.keys( ) :
                    note = self.db_dict[ key ] 
                    file.write( self.reformat_note( note ) )  
        else :
            self.logger.print_error( "DB not initialized!" )
            return 

    # UTILITIES FUNCTIONS
    def print_dict( self ) :  
        for key in self.db_dict.keys( ) :
            note = self.db_dict[ key ]
            print( f"\t PRINTING NOTE WITH ID : { key }" ) 
            note.print_note( new_line_char = self.NEW_LINE_CHAR ) 
            print( "---" ) 

    def print_unique_tags( self ) :
        for tag in self.unique_tags :
            print( tag )


