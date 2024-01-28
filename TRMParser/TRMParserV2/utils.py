import csv
from function import Function
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


# Gets the file with all the functions and associations to sys, physical and pid and parse it, creating a list of "function" objects.
def parseFunctionList( p ):

        functionList = [ ]
        with open( p ) as csv_file:
            csv_reader = csv.reader( csv_file , delimiter=';')
            for row in csv_reader:

                currentFunction = Function( row[ 0 ] , row[ 1 ] , row[ 2 ] , row[  3] )
                functionList.append( currentFunction )
        return functionList

# Finds the deepest level in the entries. The catching of the error is because, for some reason, the firs level (1) has some strange characters before it.
def findMaxLevel( entries ):

    max = 0
    for i in range( len( entries ) ):

        try:
            currentValue = int( entries[ i][ 0] )
        except:
            continue
        if( currentValue > max ):
            max = int( entries[ i ][ 0 ] )

    return max

# Takes as input the parsed entries file and the function list and associates to every function its set of requirements. Also calculate
# the number of requirements in each release state.
# Iterates on all the entries, finds a match to a function (using the PID value), and then find all the elements that: are requirements and are at least a level
# deeper than where the function name is. It stops when the max level is reached, or the depth of the function name is reached, or the end of the file is reached.
def populateRequirements( entries , functionList ):

    maxLevel = findMaxLevel( entries )
    for i in range( len( entries ) ):

        for j in range( len( functionList ) ):

            if( functionList[ j ].getPid() in entries[ i ][ 1 ]  ):

                currentLevel = entries[ i ][ 0 ]
                k = i + 1

                while( entries[ k ][ 0 ] != currentLevel and k < ( len( entries ) - 1 ) and int( entries[ k ][ 0 ] ) < maxLevel ):

                    if( "req" in entries[ k ][ 2 ] ):
                        functionList[ j ].appendReq( entries[ k ][ 3 ] )

                        if(  ( "In corso" in entries[ k ][ 4 ] ) or  ( "In Work" in entries[ k ][ 4 ] ) ):
                            functionList[ j ].increseNumInWork()
                        if( ( "Congelato" in entries[ k ][ 4 ] ) or ( "Frozen" in entries[ k ][ 4 ] ) ):
                            functionList[ j ].increseFrozen()
                        if( ( "Rilasciato" in entries[ k ][ 4 ] ) or ( "Released" in entries[ k ][ 4 ]) ):
                            functionList[ j ].increseReleased()
                    k = k + 1

    return functionList


def printFunctionBreakedown( functionList ):

    for i in range( len( functionList ) ):
        print("Function Name: " + functionList[ i ].getName( ) )
        print("Function Pid: " + functionList[ i ].getPid( ) )
        print("Function SysElement: " + functionList[ i ].getSyselement( ) )
        print("Function PhysElement: " + functionList[ i ].getPhys( ) )
        print("Function N° Reqs: " + str( len( functionList[ i ].getReqlist() ) ) )
        print("N° Reqs in work: " + str( functionList[ i ].getNumInWork( ) ) )
        print("N° Reqs released: " + str( functionList[ i ].getNumReleased( ) ) )
        print("N° Reqs frozen: " + str( functionList[ i ].getNumInFrozen( ) ) )
        print("----")

def populateOutputFile( path , functionList ):

    out = open( path , "w" )

    # Header
    out.write( "Physical Element ; System Element ; Function Name ; PID ; N° in work ; N° Released ; N° Frozen ; Total \n" )

    for i in range( len( functionList ) ):

        out.write(functionList[ i ].getPhys() + ";")
        out.write(functionList[ i ].getSyselement() + ";")
        out.write( functionList[ i ].getName(  ) + ";" )
        out.write( functionList[ i ].getPid( ) +  ";" )
        out.write( str( functionList[ i ].getNumInWork() ) + ";")
        out.write( str( functionList[ i ].getNumReleased() ) + ";")
        out.write( str( functionList[ i ].getNumInFrozen() ) + ";")
        out.write( str( functionList[ i ].getNumInWork() + functionList[ i ].getNumReleased() + functionList[ i ].getNumInFrozen() ) )
        out.write( "\n" )

    out.close()

# Remove the lines until the header one. We are just interested in everything that is below that line.
def removeExcessLines( entries ):

    l = len( entries )
    i = 0
    while( entries[ i ][ 0 ] != "Level" ):
        i = i + 1

    return entries[ i + 1 : l ]




