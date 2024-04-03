

class ImagePoint :
    
    def __init__( self , name , red , green , blue ) :
        
        self.name = name
        self.red = float( red )
        self.green = float( green )
        self.blue = float( blue)
        
        
    def print( self ) :
        print( f"Name : {self.name} - R : {self.red} - G : {self.green} - B : {self.blue} " )