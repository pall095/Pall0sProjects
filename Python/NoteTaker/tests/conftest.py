import pytest
from pathlib import Path
from src.database_manager.DatabaseManager import DatabaseManager

DB_PATH = Path(__file__).parent / "test_notes.db"

@pytest.fixture(scope="module")
def db():
    if DB_PATH.exists():
        DB_PATH.unlink()

    database = DatabaseManager(str(DB_PATH))
    database.initialize_database( )
    yield database

