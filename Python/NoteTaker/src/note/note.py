from datetime import datetime
from pathlib import Path
from uuid import uuid4
from pydantic import BaseModel, Field, ConfigDict
from src.io_manager.io_static import IOStatic

class Note(BaseModel):

    model_config = ConfigDict(extra="forbid")

    note_id: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    content: str
    tags: set[str] = Field(default_factory=list)
    links: set[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now().astimezone())

    @classmethod
    def from_yaml(cls, path: str | Path) -> "Note":

        data = IOStatic.read_yaml( path )
        if not isinstance(data, dict):
            raise ValueError("YAML file must contain a mapping.")

        return cls.model_validate(data)


    def to_yaml(self, path: str | Path) -> None:
        data = self.model_dump(mode="json")
        data["content"] = data["content"].rstrip("\n")
        IOStatic.write_yaml( path , data )

    def __str__(self) -> str:
        return (
            f"note_id: { self.note_id }\n"
            f"title: { self.title }\n"
            f"tags: { self.tags }\n"
            f"content: { self.content }\n"
            f"created_at: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"links: { self.links }\n" 
        )

    def recap_note( self ) :
        return f"Note id: { self.note_id } | Created At: { self.created_at } | Title: { self.title } | Tags: { self.tags } | Num Links: { len( self.links )} "

    def __eq__(self, other):

        if not isinstance(other, Note):
            return NotImplemented

        if self.note_id != other.note_id:
            return False
        if self.title != other.title:
            return False
        if self.tags != other.tags:
            return False
        if self.content != other.content:
            return False
        if self.created_at != other.created_at:
            return False
        if self.links != other.links:
            return False
        return True