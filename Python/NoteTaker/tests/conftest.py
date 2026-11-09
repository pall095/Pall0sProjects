import pytest
from pathlib import Path
from src.database_manager.DatabaseManager import DatabaseManager

import pytest
from src.database_manager.DatabaseManager import DatabaseManager


@pytest.fixture
def db(tmp_path):

    database = DatabaseManager.from_yaml(
        r"tests\test_database_config.yaml"
    )

    # Override configuration paths for testing
    database.db_path = tmp_path / "test_notes.db"
    database.output_folder = tmp_path / "test_files"

    database.initialize()

    yield database