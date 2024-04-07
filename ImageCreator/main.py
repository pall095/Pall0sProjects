import cv2 as cv
from DatabaseHandler import *
import os
import copy

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    

    size = 1000
    output_size = ( size , size )
    num_blocks = 50
    block_size = int( output_size[ 0 ] / num_blocks )
    
    database_path = r"C:\Users\matte\Desktop\Git\Pall0sProjects\ImageCreator\database.txt"


    img_original = cv.imread( "Image.jpg" )
    img_original = cv.resize( img_original , dsize = output_size )

    rectangle_color = ( 0 , 255 , 0 )
    rectangle_thickness = 1
    
    dbHandler = DatabaseHandler( )
    dbHandler.loadFromFile( database_path )


    try :

        for row in range( 0 , output_size[ 0 ] , block_size ):
            for col in range( 0 , output_size[ 1 ] , block_size ):
    
                img_show = img_original
                roi = copy.deepcopy( img_original[ row : row + block_size , col : col + block_size ] )
                substitute = cv.resize( dbHandler.findClosest( roi , allow_repetition = True ) , dsize = ( block_size ,  block_size ) )
                img_show[ row : row + block_size , col : col + block_size ] = substitute 
                cv.imshow( "Image" ,  img_show )
                k = cv.waitKey( 1 )          
                print( f"Percentage completion: {round( (row * size + col) / (size * size ) * 100 , 2 )} %")         
                if k == 27 :        
                    cv.waitKey( 0 )
                    cv.destroyAllWindows( )
                    break
                cv.waitKey( 1 )
            if k == 27 :
                break                       
        cv.waitKey( 0 )
        cv.destroyAllWindows( )
        
    except Exception as s:
        
        print( s )
        cv.waitKey( 0 )
        cv.destroyAllWindows( )



