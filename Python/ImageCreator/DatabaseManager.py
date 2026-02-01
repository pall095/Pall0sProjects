import os
import cv2 as cv
import json
import math 
import sys

class DatabaseManager :

    _instance = None 
    RED_KEY = "Red"
    GREEN_KEY = "Green"
    BLUE_KEY = "Blue"
    NUM_USAGE = "NUsage"
    IS_BLACKLISTED = "Blacklisted"
    MP4_EXT = ".mp4"
    JSON_EXT = ".json"

    def __init__( self , folder_path : str ) :
        
        if DatabaseManager._instance is not None :
                raise Exception( "Use init_from_folder to instantiate a new manager." )
        
        self.folder_path = folder_path
        self.database_dict = dict( )
        self.is_initialized = False 

    @classmethod
    def init_from_folder( cls , folder_path ) :

        if cls._instance == None :
            cls._instance = cls( folder_path )

        cls._instance.parse_folder( )
        return cls._instance
    

    def parse_folder( self ) :

        files_list = os.listdir( self.folder_path ) 

        total_files = len( os.listdir( self.folder_path ) ) 

        for index , file in enumerate( os.listdir( self.folder_path ) ) :
            
            print( f"{ round( index / total_files * 100 , 2 )  } % done" ) 

            if file.endswith( DatabaseManager.MP4_EXT ) : continue
            if file.endswith( DatabaseManager.JSON_EXT ) :
                 self.load_database( os.path.join( self.folder_path , file ) ) 
                 print( "Database found... Stopping images parsing" ) 
                 break 

            image = cv.imread( os.path.join( self.folder_path , file ) ) 
            ( red , green , blue , _ ) = cv.mean( image )
            self.database_dict[ file ] = { 
                 DatabaseManager.RED_KEY : red ,
                 DatabaseManager.GREEN_KEY : green ,
                 DatabaseManager.BLUE_KEY : blue ,
                 DatabaseManager.NUM_USAGE : 0 ,
                 DatabaseManager.IS_BLACKLISTED : False 
            }
        
        self.is_initialized = True 

    def dump_database( self , out_file ) :
         
         with open( os.path.join( self.folder_path ,  out_file + DatabaseManager.JSON_EXT ) , "w" ) as json_out :
              json.dump( self.database_dict ,  json_out , indent = 4 )

    def load_database( self , database_path ) :
        
        with open( database_path , "r" ) as json_in :
             self.database_dict = json.load( json_in )


    def find_closest( self , reference_image , allow_repetition ) :
         
        min = sys.float_info.max
        ( ref_red , ref_green , ref_blue , _ ) = cv.mean( reference_image )

        for key , value in self.database_dict.items() :
             
            distance = math.sqrt( pow( ref_red - value[ DatabaseManager.RED_KEY ] ,  2 ) + 
                                pow( ref_green - value[ DatabaseManager.GREEN_KEY ] ,  2 ) +
                                pow( ref_blue - value[ DatabaseManager.BLUE_KEY ] ,  2 ) ) 
        
            if distance < min and self.database_dict[ key ][ DatabaseManager.IS_BLACKLISTED ] == False :

                if allow_repetition == False and self.database_dict[ key ][ DatabaseManager.NUM_USAGE ] > 0 :   
                    continue
                else :
                    min = distance 
                    best_fit = key 


        r = cv.imread( os.path.join( self.folder_path , best_fit ) )
        if r is None :
            self.database_dict[ best_fit ][ DatabaseManager.IS_BLACKLISTED ] = True 
            print( "recursive call")
            return self.find_closest( reference_image ) 
        else :
            self.database_dict[ best_fit ][ DatabaseManager.NUM_USAGE ] += 1 
            return r 

            
