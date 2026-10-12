from typing import override

class Requirement( ) :

    def __init__( self , id , content , title , path ) :
        self.id = id
        self.content = content
        self.title = title
        self.path = path

    @classmethod
    def from_csv_row( cls , row_content ) :
        return cls( 
            id = row_content[ "ID" ] ,
            content = row_content[ "Content" ] ,
            title = row_content[ "Title" ] ,
            path = row_content[ "Path" ] ,
        )


    def print_indented( self , indentation_level = 0 ) :
        indent = "    " * indentation_level 
        for line in self.__str__( ).split( "\n" ) :
            print( indent +  line )

    @override
    def __str__( self ) :
        lines = list( ) 
        lines.append( f"ID : { self.id } - Path : { self.path }" )
        lines.append( "Title: " + self.title )
        lines.append( "Content :\n" + self.content )
        return "\n".join( lines )