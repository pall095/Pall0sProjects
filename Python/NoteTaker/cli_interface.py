
import argparse
import json
import sys

from src.database_manager.DatabaseManager import DatabaseManager
from src.database_manager.Note import Note


def main():
    parser = argparse.ArgumentParser(
        description="CLI for managing notes."
    )

    # BASIC ARGUMENTS
    parser.add_argument(
        "--db",
        default="notes.db",
        help="Path to the SQLite database (default: notes.db)"
    )

    parser.add_argument(
        "--out_folder" ,
        required = True ,
        help = "Destnation folder in which the database will dump"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # ADD
    add_parser = subparsers.add_parser(
        name ="add",
        help = "Allow to add a note to the databset"
    )

    add_parser.add_argument(
        "--note_path" ,
        required = True , 
        help = "Note to yaml file containing the note."
    )

    # Initialize
    add_parser = subparsers.add_parser(
        name ="init",
        help = "Initializes database"
    )

    #Dump
    dump_parser = subparsers.add_parser(
        name = "dump" ,
        help = "Dump results of the query to output folder" 
    )

    dump_parser.add_argument(
        "--query" ,
        required = True ,
        help = "Query to execute and dump" 
    )

    #Sync
    sync_parser = subparsers.add_parser(
        name = "sync" ,
        help = "Syncs output folder to databse" 
    )



    args = parser.parse_args() 
    command = args.command
    db = DatabaseManager(
        db_path = args.db ,
        output_folder = args.out_folder 
    )

    if command == "init" :
        db.initialize( ) 

    elif command == "add" :
        db.insert_note( Note.from_yaml( args.note_path ) )

    elif command == "dump" :
        db.dump_query_to_yaml(
            query = args.query 
        )
    elif command == "sync" :
        db.sync( )


        


    
if __name__ == "__main__":
    main()
