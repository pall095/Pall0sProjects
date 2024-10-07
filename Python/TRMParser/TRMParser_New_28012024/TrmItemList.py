from TrmItem import TrmItem
import csv

class TrmItemList:
    
    
    # CONSTRUCTOR only create an emtpy list.
    def __init__( self ) :
        
        self.list = [ ]
        
    # Method : printItemList
    # Description : print every TrmItem, using printTrmItem classmethod, in the given list.
    def printItemList( self ):
        
        for item in self.list :
            item.printTrmItem( )
            print( "----")
            

    # Method : populateFromCsv
    # Description : parse the CSV file exported from TRM filling the list with instances of TRM items.
    #               Starts parsing only after having found a line containing the word "Level" (this row is still ignored). We do not need
    #               anything before that. It also discards empty rows.
    #               Takes path to file and delimiter as argument( delimiter is just for flexibilty )
    #               Initialize first node as root.
    def pupulateFromCsv( self , path , delimiter ):
        
        self.list.append( TrmItem( 0 , "root", "root" , "root" , "root" , "root" ) )
        
        with open( path ) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = delimiter )
            ready_to_parse = False
            
            for row in csv_reader :
            
                if len( row ) == 0 : continue 
                if ready_to_parse :
                    self.list.append( TrmItem( row[ 0 ] , row[ 1 ] ,row[ 2 ] , row[ 3 ]  , row[ 4 ] ,  row[ 5 ] ) )
                if row[ 0 ] == "Level" : ready_to_parse = True 
                
    
    # Method: findFather
    # Description : goes trough the item list. Given the current i-th assign the father with the following logic:
    # 1) If the level of the current item is equal to the level of the previous one, they have the same father.
    # 2) If the level of the current item is greater by 1 of the level of the previous one, then the previous element is the father of the current one.
    # 3) If the level of the current item is simaller then the previous one (e.g. a subsection has been closed), then rolls back the list until he finds an element
    #    at the same level of the current one. Then they have the same father.
    def findFather( self ):

        for i in range( 1 , len( self.list) ) :
            
            if self.list[ i ].level == self.list[ i - 1 ].level : self.list[ i ].father = self.list[ i - 1 ].father 
            elif self.list[ i ].level == self.list[ i - 1 ].level + 1 : self.list[ i ].father = self.list[ i -  1 ]
            elif self.list[ i ].level < self.list[ i - 1 ].level :
                j = i - 1
                while j >= 0 and self.list[ j ].level >= self.list[ i ].level :
                
                    if self.list[ j ].level == self.list[ i ].level:
                        self.list[ i ].father = self.list[ j ].father 
                    j = j - 1 
                    
            
            self.list[ i ].father.childerList.append( self.list[ i ] )
            self.list[ i ].father.isFather = True
                    
                
        
        
                        
                
    
    
        