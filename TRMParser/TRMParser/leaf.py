class Leaf:

    def __init__(self , level, title, type , content , status ):

        self.level = level
        self.title = title
        self.type = type
        self.content = content
        self.status = status
        self.childrenList = [ ]


    def getLevel( self ):
        return self.level
    def setLevel( self , l ):
        self.level = l

    def getTitle( self ):
        return self.title
    def setTitle( self , t ):
        self.title = t

    def getType( self ):
        return self.type
    def setType( self ,  t):
        self.type = t

    def getContent( self ):
        return self.content
    def setContent( self , c ):
        self.content = c

    def getChildrenList( self ):
        return self.childrenList
    def appendChildrenList( self , fl ):
        self.childrenList.append( fl )

    def getStatus( self ):
        return self.status
    def setStatus( self , s ):
        self.status = s


    def printChildren( self ):

        for i in range( len( self.childrenList ) ):

            print( "  " * self.childrenList[ i ].getLevel() +  self.childrenList[ i ].title )



