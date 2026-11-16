
import pytest
from pathlib import Path
from src.note_taker.note_taker import NoteTaker
from src.note.note import Note
from datetime import datetime
import copy


def test_parse_complete_note( ):
    expected_note = {
        "note_id" : "0775bbbf-c9a9-48b4-b040-88e913b05948" ,
        "title": "Implement YAML support",
        "content": "This is the content.",
        "tags": {"tag1" , "tag2" , "tag3" } ,
        "created_at": datetime(2026, 1, 1, 0, 0) ,
        "updated_at": datetime(2026, 1, 1, 0, 0) ,
        "links" : {
            r'C:\Users\matte\Desktop\Git\Pall0sProjects\Python\NoteTaker_test_link_1' ,
            r'C:\Users\matte\Desktop\Git\Pall0sProjects\Python\NoteTaker_test_link_2'
        }
    }

    note = Note.from_yaml( r"tests\test_files\note1_complete.yaml" )
    assert note.title == expected_note[ "title" ] 
    assert note.content == expected_note[ "content" ]
    assert note.tags == expected_note[ "tags" ] 
    assert note.created_at == expected_note[ "created_at" ]
    assert note.updated_at == expected_note[ "updated_at" ]
    assert note.note_id == expected_note[ "note_id" ]
    assert note.links == expected_note[ "links" ]

def test_parse_incomplete_note( ):
    expected_note = {
        "title": "Implement YAML support",
        "content": "This is the content.",
        "tags": {"tag4" , "tag5" } ,
        "links" : {
            r'C:\Users\matte\Desktop\Git\Pall0sProjects\Python\NoteTaker_test_link_3' ,
            r'C:\Users\matte\Desktop\Git\Pall0sProjects\Python\NoteTaker_test_link_4'
        }
    }

    note = Note.from_yaml( r"tests\test_files\note2_incomplete.yaml" )
    assert note.title == expected_note[ "title" ] 
    assert note.content == expected_note[ "content" ]
    assert note.tags == expected_note[ "tags" ] 
    assert isinstance( note.created_at , datetime )
    assert isinstance( note.updated_at , datetime )
    assert note.updated_at == note.updated_at
    assert note.note_id != ""
    assert note.links == expected_note[ "links" ]

def test_note_equality( ):
    note1 = Note.from_yaml( r"tests\test_files\note3_complete.yaml" )
    note2 = Note.from_yaml( r"tests\test_files\note3_order_shuffle.yaml" )
    assert note1 == note2

def test_note_inequality( ):
    note1 = Note.from_yaml( r"tests\test_files\note2_incomplete.yaml" )
    note2 = Note.from_yaml( r"tests\test_files\note2_incomplete.yaml" )
    assert not( note1 == note2 )


def test_statistics( taker ):
    note1 = Note.from_yaml( r"tests\test_files\note1_complete.yaml" )
    note2 = Note.from_yaml( r"tests\test_files\note2_incomplete.yaml" )
    note3 = Note.from_yaml( r"tests\test_files\note3_complete.yaml" )
    taker.db_manager.insert_multiple_notes( [ note1 , note2 , note3 ] ) 
    assert taker.count_notes( ) == 3
    assert len( taker.get_tags( ) ) == 5
    assert len( taker.get_links( ) ) == 4

def test_insert_notes_and_delete( taker ):
    note1 = Note.from_yaml( r"tests\test_files\note1_complete.yaml" )
    note2 = Note.from_yaml( r"tests\test_files\note3_complete.yaml" )
    taker.db_manager.insert_multiple_notes( [ note1 , note2 ] ) 
    assert taker.count_notes( ) == 2
    taker.db_manager.delete_id( note1.note_id )
    taker.db_manager.delete_id( note2.note_id ) 
    assert taker.count_notes( ) == 0

def test_insert_notes_from_path_and_dump( taker ):
    notes =[ r"tests\test_files\note1_complete.yaml" , r"tests\test_files\note2_incomplete.yaml" ]
    taker.db_manager.insert_multiple_notes( notes ) 
    assert taker.count_notes( ) == 2

    query = """
        SELECT *
        FROM Notes
    """
    taker.get_notes_by_specific_query(
        query=query ,
        actions = [ "save" ]
    )
    output_files = list( taker.io_manager.output_folder.glob("*.yaml"))
    print( output_files )
    assert len(output_files) == 2

# Here I use 
def test_update_note(taker):
    note_path = r"tests\test_files\note3_complete.yaml"
    original_note = Note.from_yaml(note_path)
    copy_of_original_note = copy.deepcopy( original_note ) 
    taker.insert_note(note_path)

    copy_of_original_note.content = "Content 3 post update."
    copy_of_original_note.tags.add("new_tag")
    copy_of_original_note.links.add("new_link")

    taker.db_manager.update_note( copy_of_original_note )
    updated_note = taker.get_note( original_note.note_id)
    assert copy_of_original_note == updated_note
    assert updated_note.created_at == original_note.created_at
    assert updated_note.updated_at != original_note.updated_at


def test_sync(taker, tmp_path, monkeypatch):

    # 1. Insert original note into database
    note_path = r"tests\test_files\note3_complete.yaml" 
    note = Note.from_yaml( note_path )
    taker.insert_note( note_path )

    # 2. Prepare updated version
    updated_note = copy.deepcopy(note)
    updated_note.content = "Content after sync."
    updated_note.links.add( "new_link")
    updated_note.tags.add( "new_link")

    # 3. Create corresponding YAML file
    sync_file = tmp_path / f"{note.note_id}.yaml"
    sync_file.touch()

    # 4. Configure sync directory
    taker.io_manager.output_folder = tmp_path

    # 5. Mock YAML parser
    monkeypatch.setattr(
        Note,
        "from_yaml",
        staticmethod(lambda _: updated_note)
    )

    # 6. Run synchronization
    taker.sync_database()
    # 7. Verify database was updated
    stored_note = taker.get_note(note.note_id)

    assert stored_note == updated_note