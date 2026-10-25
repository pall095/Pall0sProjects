from src.database_manager.Note import Note
from src.database_manager.DatabaseManager import DatabaseManager


INITIALIZE = True 

database = DatabaseManager( r"tests\debug_db.db" ) 

if INITIALIZE :
    database.initialize_database( )

note1 = Note.from_yaml( r"tests\test_files\note1.yaml" )
note2 = Note.from_yaml( r"tests\test_files\note2.yaml" )
database.insert_multiple_notes( [ note1 , note2 ] )

for note in database.get_notes( ) :
    print( note )

