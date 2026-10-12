
import argparse
import json
import sys

from src.database_manager.NoteInterpreter import NoteInterpreter
from src.database_manager.DatabaseManager import DatabaseManager


def main():
    parser = argparse.ArgumentParser(
        description="CLI for managing notes."
    )

    parser.add_argument(
        "--db",
        default="notes.db",
        help="Path to the SQLite database (default: notes.db)"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    initialize_parser = subparsers.add_parser(
        "init" ,
        help = "Initializes database"
    )

    list_parser = subparsers.add_parser(
        "list",
        help="Print database contents"
    )
    list_parser.add_argument(
        "--mode",
        choices=["joined", "raw"],
        default="joined",
        help="Output mode (default: joined)"
    )

    # Add a note from a JSON file
    add_parser = subparsers.add_parser(
        "add",
        help="Add a note from a txt file"
    )
    add_parser.add_argument(
        "--txt-path",
        help="Path to the txt file containing the note"
    )

    # Delete a note by ID
    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a note by ID"
    )

    delete_parser.add_argument(
        "note_id",
        type=int,
        help="ID of the note to delete"
    )

    # Add a note from a JSON file
    execute_parser = subparsers.add_parser(
        "execute",
        help="Executes a query and return the results."  
    )

    execute_parser.add_argument( "--query" ,
                                help = "Query to be executed" ,
                                required = True )

    args = parser.parse_args()

    db = DatabaseManager(args.db)

    if args.command == "list":
        db.print_db(args.mode)

    elif args.command == "init" :
        db.initialize_database( )

    elif args.command == "add":

        note = NoteInterpreter.parse( args.txt_path )
        try:
            note_id = db.insert_note(note)
        except (ValueError, TypeError, KeyError) as exc:
            parser.error(f"Could not insert note: {exc}")

        print(f"Note inserted successfully. ID: {note_id}")

        
    elif args.command == "delete":
        if not db.note_exists(args.note_id):
            print(f"Note {args.note_id} does not exist.")
            sys.exit(1)

        db.delete_id(args.note_id)
        print(f"Note {args.note_id} deleted.")

    elif args.command == "execute" :
        for result in db.execute( query = args.query ) :
            print( result )


if __name__ == "__main__":
    main()
