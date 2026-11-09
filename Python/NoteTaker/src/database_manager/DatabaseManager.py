
import sqlite3
from pathlib import Path
import uuid
from contextlib import closing
import src.database_manager.MANAGER_QUERIES as _QUERIES
from src.database_manager.Note import Note
from typing import Any
from pathlib import Path
import shutil
import yaml



class DatabaseManager( ):

    NOTE_FIELDS = ["title", "content", "tags"]

    def __init__(self, db_path: str , output_folder : str ):
        self.db_path = Path(db_path)
        self.output_folder = Path( output_folder )

    @classmethod
    def from_yaml(cls, config_path: str | Path):

        config_path = Path(config_path)

        with config_path.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

        base_path = config_path.parent

        db_path = base_path / config["database"]["path"]
        output_folder = base_path / config["storage"]["output_folder"]

        return cls(
            db_path=db_path,
            output_folder=output_folder
    )
 
    def count_notes( self ) :
        rows = self.execute_query("SELECT COUNT(*) AS total FROM notes")
        return rows[0]["total"]

    def get_notes_id(self) -> list[str]:
        rows = self.execute_query("SELECT note_id FROM notes")
        return [row["note_id"] for row in rows]

    def get_notes_with_tags( self ) :
        return self.execute_query( "SELECT * FROM notes_with_tags" ) 

    def _row_to_note(self, row: dict[str, Any]) -> Note:
        """Reconstruct a Note object from a database row."""
        query = """
            SELECT t.name
            FROM tags AS t
            JOIN note_tags AS nt ON nt.tag_id = t.tag_id
            WHERE nt.note_id = ?
        """

        tag_rows = self.execute_query(query, (row["note_id"],))

        note_data = {
            **row,
            "tags": [tag["name"] for tag in tag_rows],
        }

        return Note.model_validate(note_data)


    def get_note(self, note_id: str) -> Note | None:
        """Retrieve a note by ID."""
        query = "SELECT * FROM notes WHERE note_id = ?"
        rows = self.execute_query(query, (note_id,))

        if not rows:
            return None

        return self._row_to_note(rows[0])


    def get_notes(self) -> list[Note]:
        """Retrieve all notes."""
        query = "SELECT * FROM notes ORDER BY created_at DESC"
        rows = self.execute_query(query)
        return [self._row_to_note(row) for row in rows]

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

    def initialize(self):

        if self.output_folder.exists():
            shutil.rmtree( self.output_folder )

        self.output_folder.mkdir(parents=True)

        if self.db_path.exists():
                self.db_path.unlink()
                
        self.execute_command( "PRAGMA foreign_keys = ON" )
        self.execute_command( _QUERIES.CREATE_NOTES_TABLE )
        self.execute_command( _QUERIES.CREATE_TAGS_TABLE )
        self.execute_command( _QUERIES.CREATE_TAG_NOTE_TABLE )
        self.execute_command( _QUERIES.CREATE_NOTES_WITH_TAG_VIEW )

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

    def update_note(self, note: Note) -> None:
        with sqlite3.connect(self.db_path) as connection:
            connection.execute("PRAGMA foreign_keys = ON")

            with connection :
                cursor = connection.execute(
                    """
                    UPDATE notes
                    SET title = ?, content = ?, created_at = ?
                    WHERE note_id = ?
                    """,
                    (
                        note.title,
                        note.content,
                        note.created_at.isoformat(),
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

    def delete_ids(self, ids_list: list[int]):
        for note_id in ids_list:
            self.delete_id(note_id)

    def delete_id(self, note_id: int):

        self.execute_command(
            "DELETE FROM notes WHERE note_id = ?",
            (note_id,)
        )
        print(f"Note {note_id} deleted.")


    def dump_query_to_yaml(
        self,
        query: str,
        params: tuple = (),
    ) -> int:
        """Dump each note returned by a query into a separate YAML file."""

        rows = self.execute_query(query, params)

        for row in rows:
            note = self._row_to_note(row)
            note.to_yaml( self.output_folder / f"{note.note_id}.yaml")

        return len(rows)

    def sync( self ) :
        # List all contents (files and folders)
        files_list = list( self.output_folder.iterdir() )
        for file in files_list :

            if file.suffix == ".yaml" :

                try :
                    updated_note = updated_note = Note.from_yaml( file )
                    stored_note = self.get_note( updated_note.note_id )
                except Exception as e :
                    print( e )
                    continue

            if stored_note is None :
                print( f"Note { updated_note.note_id } not found!" ) 
                continue

            print( f"Note { updated_note.note_id  } FOUND. " , end = "" )
            if stored_note == updated_note :
                print( "Notes are identical. Skipping update." )
                continue

            print( "Notes are different, attempting update. " , end = "" )

            try :
                self.update_note( updated_note )
                print(f"Note { updated_note.note_id } successfully updated!")
            except ValueError :
                print( "Note update failed" )
