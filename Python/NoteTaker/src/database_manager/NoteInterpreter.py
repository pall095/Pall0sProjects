from datetime import datetime, timezone

SET_TITLE = "set title:"
CONTENT_START = "start content:"
CONTENT_END = "end content:"
SET_TAGS = "set tags:"
SET_CREATED_AT = "set created_at:"
REQUIRED_FIELDS = {"title", "content", "tags" , "created_at" }

class NoteInterpreter :


    @staticmethod
    def dump( path_to_note : str , note_dict : dict ) :

        with open( path_to_note , "w" ) as file_out :
                for key , item in note_dict( ) :
                    file_out.write( f"Key: { key }" )
                    file_out.write( f"Item: { item }" )


    @staticmethod
    def parse( path_to_note : str ) :

        note_dict = {}
        content_lines = []
        parsing_content = False
        found_content_start = False

        with open(path_to_note, "r", encoding="utf-8") as file:
            for line in file:
                line = line.rstrip("\n\r")

                if parsing_content:
                    if line.strip() == CONTENT_END:
                        parsing_content = False
                    else:
                        content_lines.append(line)
                    continue

                if line.startswith(SET_TITLE):
                    note_dict["title"] = line.removeprefix(SET_TITLE).strip()

                elif line.startswith(SET_TAGS):
                    tags = line.removeprefix(SET_TAGS).strip()
                    note_dict["tags"] = [
                        tag.strip() for tag in tags.split(",") if tag.strip()
                    ]

                elif line.startswith(SET_CREATED_AT):
                    # Optional: validate the timestamp if your format is known.
                    created_at = line.removeprefix(SET_CREATED_AT).strip()
                    note_dict["created_at"] = datetime.fromisoformat(created_at).isoformat()

                elif line.strip() == CONTENT_START:
                    parsing_content = True
                    found_content_start = True

        if parsing_content:
            raise ValueError("Missing 'end content:' marker.")

        if not found_content_start:
            raise ValueError("Missing 'start content:' marker.")

        note_dict["content"] = "\n".join(content_lines)

        if "created_at" not in note_dict.keys( ) :
            note_dict["created_at"] = datetime.now().astimezone().isoformat()

        missing = REQUIRED_FIELDS - note_dict.keys()

        if missing:
            raise ValueError(f"Missing fields: {', '.join(sorted(missing))}")

        return note_dict


        


