


class Entry( ):
    
    entriesList =  [ ]
    
    def __init__( self, date , amount , description, category , subcategory , fixed : bool , comment,  month ):
        
        self.__date = date
        self.__amount = amount
        self.__descr = description
        self.__cat = category
        self.__subcat = subcategory
        self.__fixed = fixed
        self.__comment = comment
        self.__month = month
        Entry.entriesList.append( self )
        
        
    def __repr__( self ):
        
        return f"Items: ( Date ={self.date}, Amount ={self.amount } , Description ={self.descr } , Category = {self.cat } , Sub-Category = {self.subcat } \
            , Is Fixed? = {self.fixed } , Comment = {self.comment })"
    
    
    
    @classmethod
    def totalSum( cls ):       
        return sum( list( map( lambda x : x.amount , Entry.entriesList ) ) )
    
    @classmethod
    def preprocessItems( cls , items ):

        # --- PROCESSING AMOUNTS --- #
        # removing special caracters from amount.
        items[ 1 ] = float( items[ 1 ].split( " " )[ 1 ].replace( "," ,  "." ) )
        
        # --- PROCESSING FIXED --- #
        if items[ 5 ] == "TRUE" :
            items[ 5 ] = True 
        elif items[ 5 ] == "FALSE":
            items[ 5 ] = False            
            
        # --- PROCESSING MONTH --- #
        items[ 7 ] = int( items[ 7 ].split( "," )[ 0 ] )
        
        return items
                
    @classmethod
    def populateList( cls , path ):
        
        f = open( path )
        f.__next__()# <-- Skipping header line

        for line in f :
            
            items = line.split( "\t" ) #<-- Using tabbed separated values so I can use commas in the sheet.
            
            # Checking if we arrived at an empty line, means that file is over.
            if items[ 0 ] == "": 
                break
            else:
                items = Entry.preprocessItems( items )
                Entry( items[ 0 ], items[ 1 ], items[ 2 ], items[ 3 ], items[ 4 ], items[ 5 ], items[ 6 ], items[ 7 ] )
        
    @property
    def date( self ):
        return self.__date
    @date.setter
    def date( self , newDate ):
        self.__date = newDate 
        
    
    @property
    def amount( self ):
        return self.__amount 
    @amount.setter
    def amount( self , newAmount ):
        self.__amount = newAmount
        
    @property
    def descr( self ):
        return self.__descr
    @descr.setter
    def descr( self , newDescr ):
        self.__descr = newDescr
        
    @property
    def cat( self ):
        return self.__cat
    @cat.setter
    def cat( self , newCat ):
        self.__descr = newCat
        
    @property
    def subcat( self ):
        return self.__subcat
    @subcat.setter
    def subcat( self , newSubcat ):
        self.__subcat = newSubcat
        
    @property
    def fixed( self ):
        return self.__fixed
    @fixed.setter
    def fixed( self , newFixed ):
        self.__fixed = newFixed
        
    @property
    def comment( self ):
        return self.__comment
    @comment.setter
    def comment( self , newComment ):
        self.__comment = newComment
    
    @property
    def month( self ):
        return self.__month
    @comment.setter
    def month( self , newMonth ):
        self.__month = newMonth
    
    