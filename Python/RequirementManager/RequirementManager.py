from Requirement import Requirement

class RequirementManager( ) :

    def __init__( self , requirement_dict ) :
        self.requirement_dict = requirement_dict
        self.linkage_dict = dict( )

    @classmethod
    def from_data_frame( cls , data_frame , path_delimiter ) :

        requirement_dict = dict( )
        for _ , row_content in data_frame.iterrows( ) :

            path_pieces = row_content[ "Path" ].split( path_delimiter )
            ref_dict = requirement_dict

            while len( path_pieces ) > 0 : 
                piece = path_pieces.pop( 0 )

                # Chapter has not been seen before
                if not( piece in ref_dict.keys( ) ) :
                    ref_dict[ piece ] = {
                        "requirements" : list( )
                    }

                ref_dict = ref_dict[ piece ]

                # End of the chain, we need to append the requirement here
                if len( path_pieces ) == 0 :
                    ref_dict[ "requirements" ].append( Requirement.from_csv_row( row_content ) )  

        return cls( 
            requirement_dict
        )

    def print_dict_r( self , ref_obj , depth : int ) :
        prefix = "    " * depth 
        if isinstance( ref_obj , list ) :
            for item in ref_obj :
                item.print_indented( depth )
                print( prefix + "---" )
            print( prefix + "###" )
            return

        for key , item in ref_obj.items( ) :
            print( prefix + key )
            self.print_dict_r( item , depth = depth + 1 )


    def print_dict( self ) :
        depth = 0 
        self.print_dict_r( self.requirement_dict , depth )

