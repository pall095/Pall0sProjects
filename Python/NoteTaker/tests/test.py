
import pytest
from pathlib import Path
from src.database_manager.NoteInterpreter import NoteInterpreter 
from src.database_manager.DatabaseManager import DatabaseManager


def test_parse( db ):
    expected_note = {
        "title": "Test1",
        "content": "Test1 --> Line1\nTest1 --> Line2",
        "tags": [ "test_tag_1" ],
        "created_at": "2026-01-01T00:00:00",
    }

    result = NoteInterpreter.parse("tests/test_note1.txt")
    db.insert_note( result )
    assert result == expected_note

def test_no_date( db ):
    result = NoteInterpreter.parse("tests/test_no_date.txt")
    db.insert_note( result )
    assert "created_at" in result

def test_num_entries( db ):
    assert db.count_notes( ) == 2 