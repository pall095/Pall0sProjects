# Class for a TRM item in the exported CSV.
# Children list is a simple list (and not a TrmItemList due to some errors in the import)
class TrmItem: 
    
    # CONSTRUCTOR
    def __init__( self ,level , title, name , content, state, buffer ):
        
        self.level = int( level ) 
        self.title = title 
        self.name = self.cleanName( name )
        self.content = content
        self.state = state 
        self.buffer = buffer 
        self.father = None
        self.childerList = []
        self.isFather = False
        
        if "req" in name: self.isReq = True
        else: self.isReq = False
        

    # Method : cleanName
    # Description : simple method that cleans extra carachters from the name
    def cleanName( self , name ):
        
        name = name.replace( "=" ,  "" )
        name = name.replace( "\"" , "" )
        
        return name

    # Method : printTrmItem
    # Description : print a TrmItem and its attributes. Catches an attribute erro when you try to print the father of root (which is "None" )
    def printTrmItem( self ) :
        
        print( "Level: " + str( self.level ) )
        print( "Title: " + self.title )
        print( "Name: " + self.name )
        print( "Content: " + self.content )
        print( "State: " + self.state )
        print( "Buffer: " + self.buffer )
        print( "Is father?" + str( self.isFather ) )
        print( "Is requirement?: " + str( self.isReq ) )
        try: print( "Father Name: " + self.father.name )
        except AttributeError : print( "Root, no father!")


        

