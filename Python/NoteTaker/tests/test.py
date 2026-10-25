
import pytest
from pathlib import Path
from src.database_manager.DatabaseManager import DatabaseManager
from src.database_manager.Note import Note
from datetime import datetime


def test_parse( ):
    expected_note = {
        "title": "Implement YAML support",
        "content": "This is the content.",
        "tags": [ "python" , "pydantic" , "yaml" ] ,
        "created_at": datetime(2026, 1, 1, 0, 0) ,
    }

    note = Note.from_yaml( r"tests\test_files\note1.yaml" )
    assert note.title == expected_note[ "title" ] 
    assert note.content == expected_note[ "content" ]
    assert note.tags == expected_note[ "tags" ] 
    assert note.created_at == expected_note[ "created_at" ]
    assert note.note_id != ""
    
def test_insert( db ):
    note1 = Note.from_yaml( r"tests\test_files\note1.yaml" )
    note2 = Note.from_yaml( r"tests\test_files\note2.yaml" )
    db.insert_multiple_notes( [ note1 , note2 ] ) 
    assert db.count_notes( ) == 2
    
def test_dump( db , output_dir ):
    query = """
        SELECT *
        FROM Notes
    """
    db.dump_query_to_yaml(
        query=query,
        output_dir = str(output_dir)
    )
    output_files = list(output_dir.glob("*.yaml"))

    assert len(output_files) == 2

def test_update_note(db):
    note = Note.from_yaml(r"tests\test_files\note3.yaml")
    db.insert_note(note)
    note.content = "Content 3 post update."
    db.update_note(note)
    updated_note = db.get_note(note.note_id)
    assert updated_note.content == note.content