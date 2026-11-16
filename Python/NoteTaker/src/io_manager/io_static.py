
import yaml
from pathlib import Path
from typing import Any, Iterable
from src.logger.logger import AppLogger


class IOStatic:

    logger = AppLogger.get_logger()

    # --------------------------------------------------
    # YAML formatting
    # --------------------------------------------------

    class LiteralString(str):
        """String subclass serialized using YAML literal block style."""
        pass

    class CustomDumper(yaml.SafeDumper):
        pass

    CustomDumper.add_representer(
        LiteralString,
        lambda dumper, data: dumper.represent_scalar(
            "tag:yaml.org,2002:str",
            data,
            style="|"
        )
    )

    @staticmethod
    def _prepare_yaml_data(data: Any) -> Any:
        """Convert multiline strings to literal YAML block scalars."""

        if isinstance(data, str):
            if "\n" in data:
                return IOStatic.LiteralString(data)
            return data

        if isinstance(data, dict):
            return {
                key: IOStatic._prepare_yaml_data(value)
                for key, value in data.items()
            }

        if isinstance(data, list):
            return [
                IOStatic._prepare_yaml_data(item)
                for item in data
            ]

        if isinstance(data, tuple):
            return tuple(
                IOStatic._prepare_yaml_data(item)
                for item in data
            )

        return data

    # --------------------------------------------------
    # Path handling
    # --------------------------------------------------

    @staticmethod
    def _get_path(path: str | Path) -> Path:
        """Normalize input into a Path object."""
        return Path(path).expanduser()


    # --------------------------------------------------
    # Folder operations
    # --------------------------------------------------

    @staticmethod
    def clear_folder_from(
        path: str | Path,
        extensions: Iterable[str] | None = None
    ) -> None:

        path = IOStatic._get_path(path)

        if not path.exists():
            IOStatic.logger.warning(
                f"The folder {path} does not exist."
            )
            return

        if not path.is_dir():
            IOStatic.logger.exception(
                f"{path} is not a directory"
            )
            raise NotADirectoryError(path)


        for file in path.iterdir():

            if not file.is_file():
                continue

            if (
                extensions is None
                or file.suffix.lower().lstrip(".") in extensions
            ):
                IOStatic.logger.debug(f"Deleting {file}")
                file.unlink()
            
    # --------------------------------------------------
    # YAML operations
    # --------------------------------------------------

    @staticmethod
    def read_yaml(path: str | Path) -> Any:

        path = IOStatic._get_path(path)

        with path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    @staticmethod
    def write_yaml(
        path: str | Path,
        data: Any
    ) -> None:

        path = IOStatic._get_path(path)

        path.parent.mkdir(parents=True, exist_ok=True)

        data = IOStatic._prepare_yaml_data(data)

        with path.open("w", encoding="utf-8") as file:
            yaml.dump(
                data,
                file,
                Dumper=IOStatic.CustomDumper,
                sort_keys=False,
                allow_unicode=True
            )

    @staticmethod
    def get_files_in_folder(
        path: str | Path
    ):
        path = IOStatic._get_path(path)
        return [Path(p) for p in path.iterdir()]
