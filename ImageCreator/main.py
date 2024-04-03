import cv2 as cv
import time
from DatabaseHandler import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    output_size = ( 1000 , 1000 )
    delay = int( 0.1 * 1000 )
    num_blocks = 10
    block_size = int( output_size[ 0 ] / num_blocks )
    
    database_path = r"C:\Users\matte\Desktop\Git\Pall0sProjects\ImageCreator\output\output_full.txt"
    database_folder = r"C:\Users\matte\Desktop\Git\Pall0sProjects\ImageCreator\Database\Portogallo 19-26 Marzo 2024"


    img_original = cv.imread( "Image.jpg" )
    img = cv.resize( img_original , dsize = output_size )

    rectangle_color = ( 0 , 255 , 0 )
    rectangle_thickness = 1
    
    dbHandler = DatabaseHandler( )
    dbHandler.loadFromFile( database_path )
    #dbHandler.createFromFolder( database_folder )
    #dbHandler.saveDatabase( "output_redgreen.txt")
    dbHandler.printDatabase()

    for col in range( 0 , output_size[ 0 ] , block_size ):
        for row in range( 0 , output_size[ 1 ] , block_size ):

            print( f"Row: {row}")
            print( f"Col: {col}")
            img_show = img_original
            new_image = img_original
            img_show = cv.rectangle( img_show , ( row , col ) , ( row + block_size , col + block_size )  , rectangle_color , rectangle_thickness )   
            roi = img_original[ row : row + block_size , col : col + block_size ]
            substitute = dbHandler.findClosest( roi )
            substitute = cv.resize( substitute , dsize = ( block_size ,  block_size ) )
            new_image[ col : col + block_size , row : row + block_size ] = substitute 
            cv.imshow( "Roi" ,  img_show )
            cv.imshow( "Substitute" , substitute )
            cv.waitKey( delay )

    cv.destroyWindow( "Roi" )
    cv.destroyWindow( "Substitute")


