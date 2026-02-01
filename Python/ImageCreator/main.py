from DatabaseManager import DatabaseManager
import cv2 as cv
import copy


manager = DatabaseManager.init_from_folder( r"C:\Users\matte\Desktop\Defqon 2024-1-001\Defqon 2024" )
manager.dump_database( "000-output" )

size = 1000
output_size = ( size , size )
num_blocks = 500
block_size = int( output_size[ 0 ] / num_blocks )

img_original = cv.imread( r"C:\Users\matte\Desktop\Defqon 2024-1-001\Defqon 2024\20240629_151437.jpg" )
img_original = cv.resize( img_original , dsize = output_size )

rectangle_color = ( 0 , 255 , 0 )
rectangle_thickness = 1


for row in range( 0 , output_size[ 0 ] , block_size ):
    for col in range( 0 , output_size[ 1 ] , block_size ):

        img_show = img_original
        roi = copy.deepcopy( img_original[ row : row + block_size , col : col + block_size ] )
        substitute = cv.resize( manager.find_closest( roi , allow_repetition = True ) , dsize = ( block_size ,  block_size ) )
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

manager.dump_database( "000-output_updated" )
cv.waitKey( 0 )
cv.destroyAllWindows( )


