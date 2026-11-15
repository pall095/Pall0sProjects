import pytest
from pathlib import Path
from src.note_taker.note_taker import NoteTaker
import pytest



@pytest.fixture
def taker(tmp_path):

    taker = NoteTaker.from_yaml(
        r"configurations\test_database_config.yaml"
    )

    # Override configuration paths for testing
    taker.override_db_path( tmp_path / "test_notes.db" )
    taker.override_output_folder( tmp_path / "test_files" )
    taker.initialize( )

    yield taker