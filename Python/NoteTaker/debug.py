from src.database_manager.DatabaseManager import DatabaseManager
from src.database_manager.NoteInterpreter import NoteInterpreter

db = DatabaseManager( r"tests\debug_db.db" )

for note in db.execute( "SELECT * FROM notes" ) :
    NoteInterpreter.dump( "output.txt" , note )