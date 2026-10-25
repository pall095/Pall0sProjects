from datetime import datetime
from pathlib import Path
from uuid import uuid4

import yaml
from pydantic import BaseModel, Field, ConfigDict


class Note(BaseModel):

    model_config = ConfigDict(extra="forbid")

    note_id: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    content: str
    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now().astimezone())

    @classmethod
    def from_yaml(cls, path: str | Path) -> "Note":
        with Path(path).open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        if not isinstance(data, dict):
            raise ValueError("YAML file must contain a mapping.")

        return cls.model_validate(data)


    def to_yaml(self, path: str | Path) -> None:
        data = self.model_dump(mode="json")
        data["content"] = data["content"].rstrip("\n")

        with Path(path).open("w", encoding="utf-8") as file:
            yaml.safe_dump(
                data,
                file,
                sort_keys=False,
                allow_unicode=True
            )

    def __str__(self) -> str:
        return (
            f"note_id: { self.note_id }\n"
            f"title: { self.title }\n"
            f"tags: { self.tags }\n"
            f"content: { self.content }\n"
            f"created_at: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )