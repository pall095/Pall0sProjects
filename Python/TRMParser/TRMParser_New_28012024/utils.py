import csv

###############################
# DEPRECATED, it is now a method of the class TrmItemList
# Function : parseFile
# Description : parse the CSV file exported from TRM filling a list of entries.
#               Starts parsing only after having found a line containing the word "Level" (this row is still ignored). We do not need
#               anything before that. It also discards empty rows.

# Function to parse the file and append every line to entries.
# Start parsing afte
def parseFile( path ):

    entries = [ ]
    with open( path ) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        ready_to_parse = False
        
        for row in csv_reader :
        
            if len( row ) == 0 : continue 
            if ready_to_parse :
                entries.append( row )
            if row[ 0 ] == "Level" : ready_to_parse = True 
    return entries

# [DEPRECATED] - It's functionality is now taken care in "parseFile"
# Remove the lines until the header one. We are just interested in everything that is below that line.
def removeExcessLines( entries ):

    l = len( entries )
    i = 0
    while( entries[ i ][ 0 ] != "Level" ):
        i = i + 1

    return entries[ i + 1 : l ]

