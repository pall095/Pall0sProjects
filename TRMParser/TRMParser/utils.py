import csv
from leaf import Leaf
from function import Function

def parseRequirements( entries , excludeLen):

    requirements = [ ]

    for i in range( len( entries ) ):
        for i in range(len(entries)):

            if ("req" in entries[i][2] and len( entries[ i ][ 3 ] ) >= excludeLen ) :
                requirements.append( entries[ i ] )

        return requirements

###############################
# Just a simple function to iterate over the entries on the file and print them.
def printEntries( entries ):
    for i in range( len( entries ) ):

        print( entries[ i ] )

###############################
# Function to parse the file and append every line to entries.
def parseFile( path ):

    entries = [ ]
    with open( path ) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            entries.append( row )
    return entries

###############################
# function that build the tree with it's leaf.
# Read every line in entries and invockes the constructor of a life using as arguments the various item in the row.
def buildTree( entries , startLevel ):

    tree = [] ;
    i = startLevel

    while i < len( entries ):

        currentLeaf = Leaf( int( entries[ i ][ 0 ] ) , entries[ i ][ 1 ] , entries[ i ][ 2 ] , entries[ i ][ 3 ] , entries[ i ][ 4 ]  )
        tree.append( currentLeaf )
        i = i + 1

    return tree

###############################
# For every leaf in the tree, finds its children. The function is taking advante of the fact that the entries are ordered smoehow.
# Given the level of the current item i, finds all the element j that are a level deeper than i and append them to the children list of i.
# Once another item with the same level as i is found, it means we have scanned through all the sons of i (because the list is ordered) and we can pass
# to the next item.

# NOTES: probably is possible to re-assign i = j when we find the next level deeper?
def findChildren( tree ):

    for i in range( len( tree ) ):

        for j in range( i + 1 , len( tree ) ):

            if( tree[ j ].getLevel() == tree[ i ].getLevel() ):
                break

            if( tree[ j ].getLevel() == ( tree[ i ].getLevel() + 1 ) ):

                tree[ i ].appendChildrenList( tree[ j ] )

###############################
# Print the tree as a scrutcure by "tabbing" for every level.
# ISSUES: As it is, it is correct but there are repetition. It is not the structure as per TRM, but an item that is both a father and a children is printed two times.
def printStructure( tree ):

    for i in range( len( tree ) ):

        if( len( tree[ i ].childrenList ) != 0 ):
            print( "Title: " + tree[ i ].getTitle() )
            print("List of Children: " )
            tree[ i ].printChildren()
            print( "---------------------")


def parseFunctionList( p ):

        functionList = [ ]
        with open( p ) as csv_file:
            csv_reader = csv.reader( csv_file , delimiter=';')
            for row in csv_reader:

                currentFunction = Function( row[ 0 ] , row[ 1 ] , row[ 2 ] , row[  3] )
                functionList.append( currentFunction )
        return functionList


