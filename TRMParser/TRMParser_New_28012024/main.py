import csv
from TrmItemList import TrmItemList
from Function import Function

if __name__ == '__main__' :
    
    file_path = "ALCSys3Export_25Jan2024.csv"
    itemList = TrmItemList() 
    itemList.pupulateFromCsv( file_path ,  ',' )
    itemList.findFather() 
    itemList.printItemList()
    functionList = [ ]
    
    with open( "functionList.txt" ) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ";" )
        ready_to_parse = False
        
        for row in csv_reader :
    
                functionList.append( Function( row[ 0 ] , row[ 1 ] , row[ 2 ] , row[ 3 ] ) )


