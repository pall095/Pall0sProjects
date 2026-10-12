from datetime import datetime, timezone
import uuid
from typing import override

class Note :

    MANDATORY = [
        "title" ,
        "content"
    ]

    def __init__( self , note_id , title , content , tags , created_at ) :
        self.note_id = note_id 
        self.title = title
        self.content = content
        self.tags = tags 
        self.created_at = created_at

    @override
    def __str__( self ) :
        string_list = list( )
        string_list.append( f"note_id: { self.note_id}\n" )
        string_list.append( f"title: { self.title}\n" )
        string_list.append( f"tags: { self.tags}\n" )
        string_list.append( f"content: { self.content}\n" )
        string_list.append( f"created_at: { self.created_at}\n" )
        return "".join( string_list )

    def __dict__( self ) :
        return {
            "note_id" : self.note_id , 
            "title" : self.title , 
            "tags" : self.tags , 
            "content" : self.content , 
            "created_at" : self.created_at
        }

    @classmethod
    def from_dict( cls , note_dict : dict ) :

        if "created_at" not in note_dict.keys( ) :
            note_dict["created_at"] = datetime.now().astimezone().isoformat()

        if "note_id" not in note_dict.keys( ) :
            note_dict[ "note_id" ] = str(uuid.uuid4())


        missing = cls.MANDATORY - note_dict.keys()

        if missing:
            raise ValueError(f"Missing fields: {', '.join(sorted(missing))}")

        return cls( 
            note_id = note_dict[ "note_id" ] ,
            title = note_dict[ "title" ] ,
            content = note_dict[ "content" ] ,
            tags = note_dict[ "tags" ] ,
            created_at = note_dict[ "created_at" ]  
        )