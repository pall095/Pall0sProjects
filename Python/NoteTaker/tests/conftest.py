import pytest
from pathlib import Path
from src.database_manager.DatabaseManager import DatabaseManager

DB_PATH = Path(__file__).parent / "test_notes.db"
OUTPUT_PATH = Path("tests/test_outputs")


@pytest.fixture
def output_dir():
    return OUTPUT_PATH

@pytest.fixture(scope="module")
def db():

    database = DatabaseManager(str(DB_PATH) , str( OUTPUT_PATH ) )
    database.initialize_database( )
    yield database

