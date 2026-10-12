
import pytest
from pathlib import Path
from src.database_manager.NoteInterpreter import NoteInterpreter 
from src.database_manager.DatabaseManager import DatabaseManager
from src.database_manager.Note import Note


def test_parse( ):
    expected_note = {
        "title": "Test1",
        "content": "Test1 --> Line1\nTest1 --> Line2",
        "tags": [ "test_tag_1" ] ,
        "created_at": "2026-01-01T00:00:00",
    }

    note_dict = NoteInterpreter.parse("tests/test_note1.txt")
    note = Note.from_dict( note_dict )
    assert note.title == expected_note[ "title" ] 
    assert note.content == expected_note[ "content" ]
    assert note.tags == expected_note[ "tags" ] 
    assert note.created_at == expected_note[ "created_at" ]
    assert note.note_id != ""
    
def test_parse_multi_tags( ):
    note_dict = NoteInterpreter.parse("tests/test_note_multitag.txt")
    note = Note.from_dict( note_dict )
    assert len( note.tags ) == 3

def test_parse_no_date( ):
    note_dict = NoteInterpreter.parse("tests/test_no_date.txt")
    note = Note.from_dict( note_dict )
    assert note.created_at != ""

def test_db_insertion( db ):
    note1 = Note.from_dict( NoteInterpreter.parse("tests/test_note1.txt") )
    note2 = Note.from_dict( NoteInterpreter.parse("tests/test_note_multitag.txt") )
    note3 = Note.from_dict( NoteInterpreter.parse("tests/test_no_date.txt") )
    db.insert_multiple_notes( [ note1 , note2 , note3 ]) 
    assert db.count_notes( ) == 3
