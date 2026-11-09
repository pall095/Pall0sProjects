
import pytest
from pathlib import Path
from src.database_manager.DatabaseManager import DatabaseManager
from src.database_manager.Note import Note
from datetime import datetime
import copy


def test_parse( ):
    expected_note = {
        "title": "Implement YAML support",
        "content": "This is the content.",
        "tags": [ "pydantic" , "yaml" ,"python" ] ,
        "created_at": datetime(2026, 1, 1, 0, 0) ,
    }

    note = Note.from_yaml( r"tests\test_files\note1.yaml" )
    assert note.title == expected_note[ "title" ] 
    assert note.content == expected_note[ "content" ]
    assert note.tags == expected_note[ "tags" ] 
    assert note.created_at == expected_note[ "created_at" ]
    assert note.note_id != ""
    
def test_insert_notes_and_delete( db ):
    note1 = Note.from_yaml( r"tests\test_files\note1.yaml" )
    note2 = Note.from_yaml( r"tests\test_files\note2.yaml" )
    db.insert_multiple_notes( [ note1 , note2 ] ) 
    assert db.count_notes( ) == 2
    db.delete_id( note1.note_id )
    db.delete_id( note2.note_id ) 
    assert db.count_notes( ) == 0

def test_insert_notes_from_path_and_dump( db ):
    notes =[ r"tests\test_files\note1.yaml" , r"tests\test_files\note2.yaml" ]
    db.insert_multiple_notes( notes ) 
    assert db.count_notes( ) == 2

    
    query = """
        SELECT *
        FROM Notes
    """
    db.dump_query_to_yaml(
        query=query
    )
    output_files = list( db.output_folder.glob("*.yaml"))
    assert len(output_files) == 2

def test_update_note(db):
    note = Note.from_yaml(r"tests\test_files\note3.yaml")
    db.insert_note(note)
    note.content = "Content 3 post update."
    db.update_note(note)
    updated_note = db.get_note(note.note_id)
    assert updated_note == note


def test_sync(db, tmp_path, monkeypatch):

    # 1. Insert original note into database
    note = Note.from_yaml(r"tests/test_files/note3.yaml")
    db.insert_note(note)

    # 2. Prepare updated version
    updated_note = copy.deepcopy(note)
    updated_note.content = "Content after sync."

    # 3. Create corresponding YAML file
    sync_file = tmp_path / f"{note.note_id}.yaml"
    sync_file.touch()

    # 4. Configure sync directory
    db.output_folder = tmp_path

    # 5. Mock YAML parser
    monkeypatch.setattr(
        Note,
        "from_yaml",
        staticmethod(lambda _: updated_note)
    )

    # 6. Run synchronization
    db.sync()

    # 7. Verify database was updated
    stored_note = db.get_note(note.note_id)

    assert stored_note == updated_note