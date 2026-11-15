from src.note_taker.note_taker import NoteTaker
import argparse

import argparse
from src.note_taker.note_taker import NoteTaker

parser = argparse.ArgumentParser(
    description="CLI for managing notes."
)

parser.add_argument(
    "--config",
    required=True,
    help="YAML file containing the database configuration."
)

parser.add_argument(
    "--method",
    required=True,
    choices=[ 
             "recap" ,
             "stats" ,
             "all_notes", 
             "all_tags" , 
             "all_titles" , 
             "all_links" ,
             "by_tags", 
             "by_title", 
             "by_query" ],
    help="Search method."
)

parser.add_argument(
    "--tags",
    nargs="+",
    help="One or more tags to search for."
)

parser.add_argument(
    "--title",
    type=str,
    help="Title substring to search for."
)

parser.add_argument(
    "--query",
    type=str,
    help="Query to execute."
)


parser.add_argument(
    "--actions",
    required = False ,
    choices = [ "print" , "save" ] ,
    nargs="+" ,
    default = [ "print" ] ,
    help="Action to perform on executed search."
)

args = parser.parse_args()
taker = NoteTaker.from_yaml(args.config)

if args.method == "all_notes" :
    notes = taker.get_all_notes( actions = args.actions )

elif args.method == "all_tags" :
    notes = taker.get_tags( actions = args.actions )

elif args.method == "all_titles" :
    notes = taker.get_titles( actions = args.actions )

elif args.method == "all_links" :
    notes = taker.get_links( actions = args.actions )

elif args.method == "recap" :
    notes = taker.create_recap( )

elif args.method == "stats" :
    notes = taker.create_statistics( )

elif args.method == "by_tags":
    if not args.tags:
        parser.error("--tags is required when method is 'by_tags'")
    notes = taker.get_notes_by_tags(args.tags , actions = args.actions )

elif args.method == "by_title":
    if not args.title:
        parser.error("--title is required when method is 'by_title'")

    notes = taker.get_notes_by_title(args.title , actions = args.actions) 

elif args.method == "by_query":
    if not args.query : 
        parser.error("--query is required when method is 'by_squery'")
    notes = taker.get_notes_by_specific_query( args.query , actions = args.actions )