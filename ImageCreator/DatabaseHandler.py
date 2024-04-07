from ImagePoint import *
import cv2 as cv
import os
import math
import time

class DatabaseHandler :
    
    
    def __init__( self ) :
        
        self.hasDatabase = False #basically if the Handler is initialized.
        self.isFromFile = False #If it has been initalized from file.
        self.isFromFolder = False #If it has been initialized by parsing a folder.
        self.databasePath = None 
        self.sourcePath = None
        self.databaseList = [ ]
        
    
    def checkDatabaseUsage( self ) :
        counter = 0 
        for image_point in self.databaseList :   
            if image_point.isUsed == True :
                counter = counter + 1   
        return counter / len( self.databaseList ) 
    
    def resetDatabase( self ) :
        
        for image_point in self.databaseList :
            image_point.isUsed = False
        
  
    def printDatabase( self ) :
        
        for point in self.databaseList :
            print( f"Filename: {point.name} - R : {point.red} - G : {point.green} - B : {point.blue}" )
            
    def calculateDistance( self , pointA , pointB ) :
        
        return math.sqrt(  ( ( pointA.red - pointB.red )**2 + ( pointA.green - pointB.green )**2 + ( pointA.blue - pointB.blue )**2 ) / len( self.databaseList )  )
    
    def findClosest( self , reference_image , allow_repetition = True ) :
        
        min_distance = 100000
        [ ref_blue , ref_green , ref_red , garbage ] = cv.mean( reference_image ) 
        reference_point = ImagePoint( "" , ref_red , ref_green , ref_blue )  

        for image_point in self.databaseList :
            
            current_distance = self.calculateDistance( reference_point , image_point )
            
 
            if self.checkDatabaseUsage( ) == 1 : 
                print( "Resetting database..." )
                self.resetDatabase( )
                      
            if allow_repetition == False :
                if image_point.isUsed == True :
                    continue 
            
            if current_distance < min_distance : 
                min_distance = current_distance
                substitute = image_point
         
        substitute.isUsed = True # Sfrutto che substitute ha lo stesso riferimento alla image_point che effetivamente uso.
        print( f"\t \t \t Current database usage: {round( self.checkDatabaseUsage() * 100 , 2 ) } %" )
        return cv.imread( self.sourcePath + "\\" + substitute.name )
    
    def parseDatabase( self ):
        
        f = open( self.databasePath )    
        
        source = f.readline( )
        source = source.strip( )
        source = source.split( "," )
        self.sourcePath = source[ 1 ] 
        
        for line in f :          
            line = line.strip( )
            line = line.split( "," )     
            name = line[ 0 ]
            blue = line[ 3 ] 
            green = line[ 2 ]
            red = line[ 1 ]
            self.databaseList.append( ImagePoint( name , red , green , blue ) )
             
    def loadFromFile( self , databasePath , verbose = False  ):
        
        if self.hasDatabase : 
            print( "Handler already initialized..." ) 
        else:
            self.hasDatabase = True
            self.isFromFile = True 
            self.databasePath = databasePath 
            self.parseDatabase( ) 
            if verbose : self.printDatabase( ) 
            
    def createFromFolder( self , folder_path ) :
        
        image_list = os.listdir( folder_path )
        self.sourcePath = folder_path 
        
        
        for image in image_list :
            
            if "mp4" in image: continue
            
            current_image = cv.imread( folder_path + "\\" + image )
            name = image
            [ blue , green , red , garbage ] = cv.mean( current_image ) 
            point = ImagePoint( name , red , green , blue )
            print( f"Creating database - completion percentage: { round( len(self.databaseList) / len( image_list ) * 100 , 2 )} %")
            self.databaseList.append( point )
            
        self.databasePath = folder_path
        self.hasDatabase = True
        self.isFromFolder = True 
        
    def saveDatabase( self , output_path ) :
        
        out_file = open( output_path , 'w' )
        out_file.write( "source," + self.sourcePath + "\n" )
        
        for image in self.databaseList :
            
            line= image.name + "," + str( image.red ) + "," + str( image.green ) + "," + str( image.blue )
            out_file.write( line + "\n")
            
        out_file.close( )
            
            
            
            
        