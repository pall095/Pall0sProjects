from src.database_manager.DatabaseManager import DatabaseManager
from src.database_manager.NoteInterpreter import NoteInterpreter
from src.database_manager.Note import Note


manager = DatabaseManager( r"tests\debug_db.db" )
print( manager.get_notes_with_tags( ) )