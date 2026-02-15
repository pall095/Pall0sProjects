import pandas as pd
import yaml
import json

class FileHandler :

    @staticmethod
    def read_json( file_path : str ) :
        if not( file_path.endswith( ".json" ) ) :
            raise ValueError( "file_path must end with .json" ) 
        with open( file_path , "r" ) as json_in :
            return json.load( json_in )

    @staticmethod
    def read_csv( file_path : str ) :
        if not( file_path.endswith( ".csv" ) ) :
            raise ValueError( "file_path must end with .csv" ) 
        return pd.read_csv( file_path ) 
    
    @staticmethod
    def remap_columns( frame : pd.DataFrame , mapping_dict : dict ) :
        # Checks that all the columns in the mapping dict are in the frame.
        for new_col in mapping_dict.keys( ) :
            if not( new_col in frame.columns.values.tolist( ) ) :
                raise ValueError( f"{ new_col } is not part of the original columns of the frame" )
        
        return frame.rename( columns = mapping_dict ) 
    
    @staticmethod
    def read_yaml( file_path : str ) :
        if not( file_path.endswith( ".yaml" ) ) :
            raise ValueError( "file_path must end with .yaml" ) 
        with open( file_path , "r" ) as yaml_in :
            return yaml.safe_load( yaml_in )
        
    @staticmethod
    def frame_to_csv( frame : pd.DataFrame , file_path ) :
        frame.to_csv( file_path ) 
    
    def string_to_txt( content : str | list , file_path ) :
        if not( file_path.endswith( ".txt" ) ) :
            raise ValueError( "file_path must end with .txt" ) 

        with open( file_path , "w" ) as file_out :
            if isinstance( content , str ) :
                file_out.write( content )
            elif isinstance( content , list ) :
                for s in content :
                    file_out.writelines( content ) 
            else :
                raise TypeError( f"content must be a string or a list of strings" )
        
