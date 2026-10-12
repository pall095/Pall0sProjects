
CREATE_NOTES_TABLE = """
CREATE TABLE IF NOT EXISTS notes (
    note_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL ,
    created_at TEXT NOT NULL 
)
"""


CREATE_TAGS_TABLE = """
CREATE TABLE IF NOT EXISTS tags (
    tag_id TEXT PRIMARY KEY ,
    name TEXT NOT NULL UNIQUE
    )
"""

CREATE_TAG_NOTE_TABLE = """
CREATE TABLE IF NOT EXISTS note_tags (
note_id TEXT NOT NULL,
tag_id TEXT NOT NULL,
PRIMARY KEY (note_id, tag_id),
FOREIGN KEY (note_id)
    REFERENCES notes(note_id)
    ON DELETE CASCADE,
FOREIGN KEY (tag_id)
    REFERENCES tags(tag_id)
    ON DELETE CASCADE
)
"""

CREATE_NOTES_WITH_TAG_VIEW = """
    CREATE VIEW IF NOT EXISTS notes_with_tags AS
    SELECT
        n.note_id,
        n.title,
        n.content,
        n.created_at,
        COALESCE(GROUP_CONCAT(t.name, ', '), '') AS tags
    FROM notes n
    LEFT JOIN note_tags nt ON n.note_id = nt.note_id
    LEFT JOIN tags t ON nt.tag_id = t.tag_id
    GROUP BY
        n.note_id,
        n.title,
        n.content,
        n.created_at
"""

INSERT_NOTE_PARAM = """
INSERT INTO notes (note_id, title, content, created_at)
VALUES (?, ?, ?, ?)
"""

INSERT_TAG_PARAM = """
INSERT INTO tags (tag_id, name)
VALUES (?, ?)
ON CONFLICT(name) DO NOTHING
"""

INSERT_NOTE_TAG_PARAM = """
INSERT INTO note_tags (note_id, tag_id)
VALUES (?, ?)
"""