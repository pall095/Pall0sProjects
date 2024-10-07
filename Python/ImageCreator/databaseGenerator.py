import os
import cv2 as cv


database_path = r"C:\Users\matte\Desktop\Git\Pall0sProjects\ImageCreator\Database\ShortDatabase"
image_list = os.listdir( database_path )

counter = 0
database_dict = { }


output_file = r"C:\Users\matte\Desktop\Git\Pall0sProjects\ImageCreator\output\\" + "output.txt"  

if os.path.isfile( output_file ) :
    print( "Output file already extis... Recreating")
    
output_handle = open( output_file , "w" )
    

for image in image_list:
    currentImage = cv.imread( database_path + "\\" + image )
    counter = counter + 1
    print( f"Analyzing Image number: {counter} - Completion %: { round( counter / len( image_list ) * 100 , 2 )  }")
    database_dict[ image ] =  cv.mean( currentImage )

for key , value in database_dict.items() :

    line = key
    for currentValue in value[ 0 : 3 ] :
        line = line + "," + str( currentValue )

    line = line + "\n"
    output_handle.write( line )
output_handle.close( )










