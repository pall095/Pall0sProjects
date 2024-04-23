

class Entry :
    
    
    def __init__( self , entryList ) :
        
        self.date = entryList[ 0 ]
        self.value = entryList[ 1 ]
        self.descr = entryList[ 2 ]
        self.cat = entryList[ 3 ]
        self.subcat = entryList[ 4 ]
        self.fixed = entryList[ 5 ]
        self.comments = entryList[ 6 ]
        self.month = entryList[ 7 ] 
        
        
    def printEntry( self ) :
        
        print( f"Date: {self.date} - Value: {self.value} - Descr: {self.descr} - Cat: {self.cat} - SubCat: {self.subcat} - Fixed: {self.fixed}" )