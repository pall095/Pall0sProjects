
import sqlite3
from pathlib import Path
import uuid
from contextlib import closing
import src.database_manager.MANAGER_QUERIES as _QUERIES
from src.note.note import Note
from datetime import datetime
from src.logger.logger import AppLogger

class DatabaseManager( ):

    def __init__( self , db_path ):
        self.db_path = db_path 
        self.logger = AppLogger.get_logger( )


    def initialize_database(self):                
        self.execute_command( "PRAGMA foreign_keys = ON" )
        self.execute_command( _QUERIES.CREATE_NOTES_TABLE )
        self.execute_command( _QUERIES.CREATE_TAGS_TABLE )
        self.execute_command( _QUERIES.CREATE_TAG_NOTE_TABLE )
        self.execute_command( _QUERIES.CREATE_NOTES_WITH_TAG_VIEW )
        self.execute_command( _QUERIES.CREATE_LINKS_TABLE )


    def _cleanup_orphan_tags(self):
        query = """
            DELETE FROM tags
            WHERE NOT EXISTS (
                SELECT 1
                FROM note_tags
                WHERE note_tags.tag_id = tags.tag_id
            )
        """
        self.logger.debug( "Deleting orphan tags" )
        self.execute_command( query )

    def execute_query(self, query: str, params=()) -> list[dict]:
        self.logger.debug( f"Executing query { query }" )
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

    def insert_multiple_notes( self , notes_list : list ) :
        for note in notes_list :
            self.insert_note( note )

    def insert_note(self, note: Note | str ) -> None:
        
        if isinstance( note , str ) :
            note = Note.from_yaml( note )
        elif isinstance( note , Note ) :
            pass 
        else :
            raise AttributeError( "note parameter passed to insert note must be either a not or a path to a yaml file" )

        with sqlite3.connect(self.db_path) as connection:
            connection.execute("PRAGMA foreign_keys = ON")

            with connection :

                connection.execute(
                    _QUERIES.INSERT_NOTE_PARAM,
                    (
                        note.note_id,
                        note.title,
                        note.content,
                        note.created_at.isoformat(),
                        note.created_at.isoformat()
                    ),
                )

                for tag in {tag.strip() for tag in note.tags if tag.strip()}:
                    connection.execute(
                        """
                        INSERT INTO tags (tag_id, name)
                        VALUES (?, ?)
                        ON CONFLICT(name) DO NOTHING
                        """,
                        (str(uuid.uuid4()), tag),
                    )

                    tag_id = connection.execute(
                        "SELECT tag_id FROM tags WHERE name = ?",
                        (tag,),
                    ).fetchone()[0]

                    connection.execute(
                        _QUERIES.INSERT_NOTE_TAG_PARAM,
                        (note.note_id, tag_id),
                    )

                for link in note.links :

                    connection.execute(
                        """
                        INSERT INTO note_links (
                            link_id,
                            note_id,
                            url
                        )
                        VALUES (?, ?, ?)
                        """,
                        (
                            str(uuid.uuid4()),
                            note.note_id,
                            link ,
                        )
                    )

        self.logger.info( f"Note { note.note_id } ({ note.title }) inserted.")

    def update_note(self, note: Note) -> None:
        self.logger.info( f"Attempting update of note { note.note_id }.")
        note.updated_at = datetime.now().astimezone()
        with sqlite3.connect(self.db_path) as connection:
            connection.execute("PRAGMA foreign_keys = ON")

            with connection :
                cursor = connection.execute(
                    """
                    UPDATE notes
                    SET title = ?, content = ?, created_at = ? , updated_at = ?
                    WHERE note_id = ?
                    """,
                    (
                        note.title,
                        note.content,
                        note.created_at.isoformat(),
                        note.updated_at.isoformat(),
                        note.note_id,
                    ),
                )

                if cursor.rowcount == 0:
                    raise ValueError(f"Note {note.note_id} does not exist.")

                connection.execute(
                    "DELETE FROM note_tags WHERE note_id = ?",
                    (note.note_id,),
                )

                for tag in {tag.strip() for tag in note.tags if tag.strip()}:
                    connection.execute(
                        """
                        INSERT INTO tags (tag_id, name)
                        VALUES (?, ?)
                        ON CONFLICT(name) DO NOTHING
                        """,
                        (str(uuid.uuid4()), tag),
                    )

                    tag_id = connection.execute(
                        "SELECT tag_id FROM tags WHERE name = ?",
                        (tag,),
                    ).fetchone()[0]

                    connection.execute(
                        _QUERIES.INSERT_NOTE_TAG_PARAM,
                        (note.note_id, tag_id),
                    )


                connection.execute(
                    "DELETE FROM note_links WHERE note_id = ?",
                    (note.note_id,)
                )


                for link in note.links:

                    connection.execute(
                        """
                        INSERT INTO note_links (
                            link_id,
                            note_id,
                            url
                        )
                        VALUES (?, ?, ?)
                        """,
                        (
                            str(uuid.uuid4()),
                            note.note_id,
                            link
                        )
                    )
        self.logger.info( "Update complete." )

    def delete_ids(self, ids_list: list[int]):
        for note_id in ids_list:
            self.delete_id(note_id)

    def delete_id(self, note_id: int):
        self.execute_command(
            "DELETE FROM notes WHERE note_id = ?",
            (note_id,)
        )
        self.logger.info(f"Note {note_id} deleted.")
        self._cleanup_orphan_tags( )



