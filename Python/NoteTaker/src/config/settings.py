from pathlib import Path
from pydantic import BaseModel, ConfigDict
from typing import Literal



class DatabaseConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    path: Path


class StorageConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    output_folder: Path


class SettingsConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    autoclear_output: bool = False
    verbosity_level: Literal[
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL"
    ] = "INFO"


class AppConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    database: DatabaseConfig
    storage: StorageConfig
    settings: SettingsConfig = SettingsConfig()