


from pathlib import Path
from src.database_manager.database_manager import DatabaseManager
from src.io_manager.io_manager import IOManager
from src.config.settings import AppConfig
from src.logger.logger import AppLogger
from src.note.note import Note
from functools import wraps
from typing import Any


class NoteTaker( ) :

    def __init__(self, db_path: str , 
                 output_folder : str , 
                 autoclear_output : bool ,
                 verbosity_level : str ):
        
        AppLogger.configure(verbosity_level)
        self.io_manager = IOManager( db_path , output_folder , autoclear_output )
        self.db_manager = DatabaseManager( db_path )
        self.logger = AppLogger.get_logger( )

    def override_db_path( self , new_db_path : str | Path ) :
        self.logger.debug( "Db path is being overwritten." )
        self.io_manager.db_path = new_db_path
        self.db_manager.db_path = new_db_path 

    def override_output_folder( self , new_output_folder : str | Path ) :
        self.io_manager.output_folder = new_output_folder 

    @classmethod
    def from_yaml(cls, config_path: str | Path):

        config_path = Path(config_path).expanduser().resolve()
        config = AppConfig.model_validate(
            IOManager.read_yaml(config_path)
        )
        base_path = config_path.parent
        db_path = base_path / config.database.path
        output_folder = base_path / config.storage.output_folder

        return cls(
            db_path=db_path,
            output_folder=output_folder,
            autoclear_output=config.settings.autoclear_output,
            verbosity_level=config.settings.verbosity_level
        )

    def action_decorator(func):
        @wraps(func)
        def wrapper( self , *args, actions=None, **kwargs):

            result = func( self , *args, **kwargs )
            items_to_save = list( )
            if actions is None:
                return result

            for item in result : 
                for action in actions :

                    if action == "print" :
                        print( item ) 
                    elif action == "save" :
                        items_to_save.append( item )
                    else : 
                        self.logger.warning( f"Unknown action { action }" )
            self.io_manager.save_notes( items_to_save )
            return result

        return wrapper

    def _row_to_note(self, row: dict[str, Any]) -> Note:
        """Reconstruct a Note object from a database row."""
        query_tags = """
            SELECT t.name
            FROM tags AS t
            JOIN note_tags AS nt ON nt.tag_id = t.tag_id
            WHERE nt.note_id = ?
            ORDER BY t.name ASC
        """

        query_links = """
            SELECT url
            FROM note_links
            WHERE note_id = ?
        """

        tag_rows = self.db_manager.execute_query( query_tags , (row["note_id"],))
        links_rows = self.db_manager.execute_query( query_links , (row["note_id"],))

        note_data = {
            **row,
            "tags": [tag["name"] for tag in tag_rows],
            "links" : [link["url"] for link in links_rows]
        }   

        return Note.model_validate(note_data)


    def initialize(self):
        self.io_manager.initalize_files( )
        self.db_manager.initialize_database( )

    def insert_note( self , note : str | Path | Note ) :
        if not isinstance( note , Note ) :
            note = Note.from_yaml( note )
        self.db_manager.insert_note( note )

    def count_notes( self ) :
        rows = self.db_manager.execute_query("SELECT COUNT(*) AS total FROM notes")
        return rows[0]["total"]

    @action_decorator
    def get_tags( self ) -> list[ str ] :
        query = "SELECT DISTINCT name from tags"
        rows = self.db_manager.execute_query( query )
        return [ d[ "name" ] for d in rows ]

    @action_decorator
    def get_links( self ) -> list[ str ] :
        query = "SELECT DISTINCT url from note_links"
        rows = self.db_manager.execute_query( query )
        return [ d[ "url" ] for d in rows ]

    def get_note(self, note_id: str) -> Note | None:
        """Retrieve a note by ID."""
        query = "SELECT * FROM notes WHERE note_id = ?"
        rows = self.db_manager.execute_query(query, (note_id,))
        if not rows:
            return None
        return self._row_to_note(rows[0])
    
    @action_decorator
    def get_all_notes(self) -> list[Note]:
        """Retrieve all notes."""
        query = "SELECT * FROM notes ORDER BY created_at DESC"
        rows = self.db_manager.execute_query(query)
        return [self._row_to_note(row) for row in rows]

    @action_decorator
    def get_titles( self ) -> list[ Note ] :
        query = "SELECT title from notes"
        rows = self.db_manager.execute_query( query )
        return [ row[ "title" ] for row in rows]
    
    @action_decorator
    def get_notes_by_title( self , title ) :
        query = "SELECT * FROM notes WHERE title LIKE ?"
        rows = self.db_manager.execute_query(query, (f"%{title}%",))

        if not rows:
            return []
        return [self._row_to_note(row) for row in rows]

    @action_decorator
    def get_notes_by_tags( self , tags : list ) :
        if not tags:
            return []

        placeholders = ", ".join("?" for _ in tags)
        query = f"""
            SELECT DISTINCT n.*
            FROM notes AS n
            JOIN note_tags AS nt ON nt.note_id = n.note_id
            JOIN tags AS t ON t.tag_id = nt.tag_id
            WHERE t.name IN ({placeholders})
            ORDER BY n.created_at DESC
        """

        rows = self.db_manager.execute_query(query, tuple(tags))
        return [self._row_to_note(row) for row in rows]

    @action_decorator
    def get_notes_by_specific_query( self , query : str ) :
        rows = self.db_manager.execute_query(query,)
        if not rows:
            return []
        return [self._row_to_note(row) for row in rows]

    def create_recap( self ) :
        notes = self.get_all_notes( ) 
        for note in notes :
            print( f"Note id: { note.note_id } | Title: { note.title } | Tags: { note.tags } | Num Links: { len( note.links )}" )

    def create_statistics( self ) :
        
        print( f"Total number of notes: { self.count_notes( ) }" ) 
        print( f"Total number of links: { len( self.get_links( ) ) }" ) 
        print( f"Total number of tags: { len( self.get_tags( ) ) }" )  
        print( "Total notes per tag:" )
        query = """
        SELECT T.name ,
                COUNT( * ) AS NumNotes 
        FROM tags as T 
        JOIN note_tags AS NT ON NT.tag_id = T.tag_id
        GROUP BY T.tag_id , T.name
        """
        num_notes_per_tags = self.db_manager.execute_query( query )
        for row in num_notes_per_tags :
            print( f"\t - { row[ "name" ] }: { row[ "NumNotes" ] }" )

    def sync_database( self ) :

        self.logger.info( f"Syncing database against { self.io_manager.output_folder }")
        updated_notes = self.io_manager.get_notes_in_output_folder( )
        self.logger.debug( f"Found { len( updated_notes ) } in output folder." )
        
        for updated_note in updated_notes :
            stored_note = self.get_note( updated_note.note_id )
            if stored_note is None :
                self.logger.info( f"Note { updated_note.note_id } not found!" ) 
                continue

            self.logger.info( f"Note { updated_note.note_id  } FOUND. " )
            if stored_note == updated_note :
                self.logger.info( "Notes are identical. Skipping update." )
                continue

            self.logger.info( "Notes are different, attempting update. " )

            try :
                self.db_manager.update_note( updated_note )
            except ValueError :
                self.logger.error( "Note update failed" )

            