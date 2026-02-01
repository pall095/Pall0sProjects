import cv2 as cv
from DatabaseHandler import *
import os
import copy

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    
    database_folder = r"C:\Users\matte\Desktop\Database\Portogallo 19-26 Marzo 2024"
    output_path = r"C:\Users\matte\Desktop\Git\Pall0sProjects\ImageCreator\database.txt"

    dbHandler = DatabaseHandler( )
    dbHandler.createFromFolder( database_folder )
    dbHandler.saveDatabase(  output_path )
    dbHandler.printDatabase()

