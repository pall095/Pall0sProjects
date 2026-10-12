from Requirement import Requirement
from typing import override

class RequirementManager( ) :

    def __init__( self , requirement_dict , title_to_ids , chapter_to_ids ) :
        self.requirement_dict = requirement_dict
        self.title_to_ids = title_to_ids
        self.chapter_to_ids = chapter_to_ids 
        self.linkage_dict = dict( )

    @classmethod
    def from_data_frame( cls , data_frame , path_delimiter ) :

        requirement_dict = dict( )
        titles_to_ids = dict( )
        chapter_to_ids = dict( )

        for _ , row_content in data_frame.iterrows( ) :

            r = Requirement.from_csv_row( row_content )
            requirement_dict[ r.id ] = r

            if r.title in titles_to_ids.keys( ) :
                titles_to_ids[ r.title ].append( r.id )
            else :
                titles_to_ids[ r.title ] = [ r.id ]

            if r.path in chapter_to_ids.keys( ) :
                chapter_to_ids[ r.path ].append( r.id ) 
            else :
                chapter_to_ids[ r.path ] = [ r.id ] 
                    
                        

        return cls( 
            requirement_dict ,
            titles_to_ids ,
            chapter_to_ids 
        )

    @override
    def __str__( self ) :
        s = [ ]
        for key , item in self.requirement_dict.items( ) :
            s.append( item.__str__() )

        s.append( self.title_to_ids.__str__( ) )
        s.append( self.chapter_to_ids.__str__( ) )
        return "\n".join( s ) 


    def query_by_id( self , id ) :
        return self.requirement_dict[ id ] 

    def query_by_title( self , title ) :
        r = list( )
        for id in self.title_to_ids[ title ] :
            r.append( self.requirement_dict[ id ] ) 
        return r 

