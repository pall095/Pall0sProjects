from Entry import Entry

class EntriesDatabase :
    
    
    def __init__( self ) :
        
        self.entries_list = [ ]
        
        
    def addParsedEntry( self , new_entry : Entry ) :
        
        self.entries_list.append( new_entry )
        

    def addUnparsedentry( self , new_entry_date , new_entry_descr , new_entry_amount ) :
             
        for entry in self.entries_list :
            
            if new_entry_descr in entry.descr :
                
                print( "Found a match:" )
                entry.printEntry( )
        
        