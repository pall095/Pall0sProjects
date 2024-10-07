# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
from utils import parseFile, parseFunctionList, populateRequirements, printFunctionBreakedown, populateOutputFile, removeExcessLines



if __name__ == '__main__':

    filepath = "ALCSys3Export_28Nov2023_Original_NotOpened_Copy.csv"
    functionListPath = "functionList_Copy.txt"
    outputFile = "Output.csv"
    entries = removeExcessLines( parseFile( filepath ) ) # Entries Structure: 0 = level | 1 = title | 2 = type | 3 = content | 4 = state
    #functionList = populateRequirements( entries , parseFunctionList( functionListPath ) )
    #printFunctionBreakedown( functionList )
    #populateOutputFile( outputFile , functionList )

    print( entries )















