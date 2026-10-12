
import sqlite3
from pathlib import Path
import uuid
from contextlib import closing
import src.database_manager.MANAGER_QUERIES as _QUERIES
from src.database_manager.Note import Note

class DatabaseManager( ):

    NOTE_FIELDS = ["title", "content", "tags"]

    def __init__(self, db_path: str):
        self.db_path = Path(db_path)
        self.initialize_database()

    def get_notes_id( self ) :
        return [ entry[ "note_id" ] for entry in self.execute_query( "SELECT note_id FROM NOTES" ) ]
        

    def print_notes_with_tags( self ) :
        for note in self.get_notes_with_tags( ) :
            print( Note.from_dict( note ) )

    def count_notes( self ) :
        rows = self.execute_query("SELECT COUNT(*) AS total FROM notes")
        return rows[0]["total"]

    def get_notes_with_tags( self ) :
        return self.execute_query( "SELECT * FROM notes_with_tags" ) 

    def execute_query(self, query: str, params=()) -> list[dict]:
        """Execute a SELECT query and return rows as dictionaries."""
        with closing(sqlite3.connect(self.db_path)) as connection:
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]

    def execute_command(self, query: str, params=()) -> int:
        """Execute an INSERT, UPDATE or DELETE and commit the transaction."""
        with closing(sqlite3.connect(self.db_path)) as connection:
            connection.execute("PRAGMA foreign_keys = ON")

            with connection:
                cursor = connection.execute(query, params)
                return cursor.rowcount

    def initialize_database(self):
            self.execute_command( "PRAGMA foreign_keys = ON" )
            self.execute_command( _QUERIES.CREATE_NOTES_TABLE )
            self.execute_command( _QUERIES.CREATE_TAGS_TABLE )
            self.execute_command( _QUERIES.CREATE_TAG_NOTE_TABLE )
            self.execute_command( _QUERIES.CREATE_NOTES_WITH_TAG_VIEW )

    def insert_multiple_notes( self , notes_list : list ) :
        for note in notes_list :
            self.insert_note( note )

        
    def insert_note(self , note : Note ):
        
        with closing(sqlite3.connect(self.db_path)) as connection:
            with connection:
                self.execute_command("PRAGMA foreign_keys = ON")

                self.execute_command(
                    _QUERIES.INSERT_NOTE_PARAM ,
                    (
                        note.note_id ,
                        note.title ,
                        note.content ,
                        note.created_at ,
                    ),
                )

                for tag in {tag.strip() for tag in note.tags }:
                    self.execute_command(
                        _QUERIES.INSERT_TAG_PARAM ,
                        (str(uuid.uuid4()), tag),
                    )

                    tag_id = self.execute_query(
                        "SELECT tag_id FROM tags WHERE name = ?",
                        (tag,),
                    )[ 0 ][ "tag_id" ]

                    self.execute_command(
                        _QUERIES.INSERT_NOTE_TAG_PARAM ,
                        ( note.note_id , tag_id),
                    )


    def delete_ids(self, ids_list: list[int]):
        for note_id in ids_list:
            self.delete_id(note_id)

    def delete_id(self, note_id: int):
        if not self.note_exists(note_id):
            print(f"Note {note_id} does not exist.")
            return

        self.execute_command(
            "DELETE FROM notes WHERE note_id = ?",
            (note_id,)
        )
        print(f"Note {note_id} deleted.")

