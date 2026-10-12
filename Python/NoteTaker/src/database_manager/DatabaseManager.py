
import sqlite3
from pathlib import Path
import uuid
from contextlib import closing
import src.database_manager.MANAGER_QUERIES as _QUERIES

class DatabaseManager( ):

    NOTE_FIELDS = ["title", "content", "tags"]

    def __init__(self, db_path: str):
        self.db_path = Path(db_path)
        self.initialize_database()

    def count_notes( self ) :
        _ , rows = self.execute( f"SELECT COUNT( * ) FROM notes"  )
        return rows[ 0 ][ 0 ]

    def execute(self, query: str, params=()):
        """Execute a query and return headers and rows for SELECTs."""
        with closing( sqlite3.connect(self.db_path) )  as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.execute(query, params)

            if cursor.description is not None:
                headers = [column[0] for column in cursor.description]
                rows = cursor.fetchall()
                return headers, rows

            return cursor.lastrowid

    def initialize_database(self):
        with closing( sqlite3.connect(self.db_path) )as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            connection.execute( _QUERIES.CREATE_NOTES_TABLE )
            connection.execute( _QUERIES.CREATE_TAGS_TABLE )
            connection.execute( _QUERIES.CREATE_TAG_NOTE_TABLE )

    def print_db(self, mode: str):
        if mode == "joined":
            
            query = _QUERIES.JOINED_NOTE_TAG_NOTE_TABLE
            headers, rows = self.execute(query)

            print("\n=== Notes with tags ===")
            print(" | ".join(headers))

            if not rows:
                print("No notes found.")
                return

            for row in rows:
                print(" | ".join(
                    str(value) if value is not None else "-"
                    for value in row
                ))

        elif mode == "raw":
            tables = ["notes", "tags", "note_tags"]

            for table in tables:
                headers, rows = self.execute(
                    f"SELECT * FROM {table}"
                )

                print(f"\n=== Table: {table} ===")
                print(" | ".join(headers))

                if not rows:
                    print("Empty table.")
                    continue

                for row in rows:
                    print(" | ".join(
                        str(value) if value is not None else "-"
                        for value in row
                    ))

        else:
            raise ValueError(
                f"Invalid mode '{mode}'. Use 'joined' or 'raw'."
            )

    def note_exists(self, note_id: int) -> bool:
        _, rows = self.execute(
            "SELECT EXISTS(SELECT 1 FROM notes WHERE note_id = ?)",
            (note_id,)
        )
        return rows[0][0] == 1


    def insert_note(self, note_dict: dict):
        missing = set(self.NOTE_FIELDS) - note_dict.keys()
        if missing:
            raise ValueError(
                f"Note definition requires: {', '.join(sorted(missing))}"
            )

        tags = note_dict["tags"]

        if isinstance(tags, str):
            raise TypeError("Tags must be a list of strings, not a string.")

        if not all(isinstance(tag, str) and tag.strip() for tag in tags):
            raise ValueError("Every tag must be a non-empty string.")

        note_id = str(uuid.uuid4())

        with closing(sqlite3.connect(self.db_path)) as connection:
            with connection:
                connection.execute("PRAGMA foreign_keys = ON")

                connection.execute(
                    _QUERIES.INSERT_NOTE_PARAM ,
                    (
                        note_id,
                        note_dict["title"],
                        note_dict["content"],
                        note_dict["created_at"],
                    ),
                )

                for tag in {tag.strip() for tag in tags}:
                    connection.execute(
                        _QUERIES.INSERT_TAG_PARAM ,
                        (str(uuid.uuid4()), tag),
                    )

                    tag_id = connection.execute(
                        "SELECT tag_id FROM tags WHERE name = ?",
                        (tag,),
                    ).fetchone()[0]

                    connection.execute(
                        _QUERIES.INSERT_NOTE_TAG_PARAM ,
                        (note_id, tag_id),
                    )

        return note_id


    def delete_ids(self, ids_list: list[int]):
        for note_id in ids_list:
            self.delete_id(note_id)

    def delete_id(self, note_id: int):
        if not self.note_exists(note_id):
            print(f"Note {note_id} does not exist.")
            return

        self.execute(
            "DELETE FROM notes WHERE note_id = ?",
            (note_id,)
        )
        print(f"Note {note_id} deleted.")
