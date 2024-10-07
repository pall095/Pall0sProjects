# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
from leaf import Leaf

from utils import printStructure, findChildren, buildTree, parseFile, parseFunctionList


if __name__ == '__main__':

    filepath = "ALCSys3Export_23Nov2023.csv"
    functionListPath = "functionList.txt"
    entries = parseFile( filepath )
    functionList = parseFunctionList( functionListPath )
    startIndex = 1
    tree = buildTree( entries , startIndex )
    findChildren( tree  )
    #printStructure( tree )

    indexOfStateMachine = 78

    #for i in range( len( tree) ):
    #    for j in range( len( functionList ) ):

    #       if(  functionList[ j ].getName() in tree[ i ].getTitle() ):













