
from src.note_taker.note_taker import NoteTaker
import argparse


parser = argparse.ArgumentParser(
    description="CLI for managing notes."
)

# Global arguments
parser.add_argument(
    "--config",
    required=True,
    help="YAML file containing the database configuration."
)

# Command dispatcher
subparsers = parser.add_subparsers(
    dest="command",
    required=True
)

# -------------------------
# INITIALIZE COMMAND
# -------------------------

init_parser = subparsers.add_parser(
    "init",
    help="Initialize."
)

# -------------------------
# SYNC COMMAND
# -------------------------

init_parser = subparsers.add_parser(
    "sync",
    help="Sync."
)

# -------------------------
# INSERT COMMAND
# -------------------------
insert_parser = subparsers.add_parser(
    "insert",
    help="Insert a note."
)

insert_parser.add_argument(
    "--path_to_note",
    required=True,
    help="Path to the note to be inserted."
)

# -------------------------
# DELETE COMMAND
# -------------------------

delete_parser = subparsers.add_parser(
    "delete",
    help="Delete a note."
)

delete_parser.add_argument(
    "--note_id",
    required=True,
    help="ID of the note to delete."
)

# -------------------------
# EXECUTION
# -------------------------

args = parser.parse_args()
taker = NoteTaker.from_yaml(args.config)

if args.command == "insert":
    taker.insert_note(args.path_to_note)

elif args.command == "delete":
    taker.db_manager.delete_id( args.note_id )

elif args.command == "init":
    taker.initialize( )

elif args.command == "sync":
    taker.sync_database( )
