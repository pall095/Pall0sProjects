

class Movement:
    
    def __init__( self , line ):
        
        self.movementDate = line[ 0 ]
        self.valueDate = line[ 1 ] 
        self.movementDescription = line[ 2 ]
        self.cause = line[ 3 ]
        self.amount = float( line[ 4 ].replace( "," , "." ) )
        self.moneyType = line[ 5 ]
        self.progressiveBalance = float( line[ 6 ].replace( "," , "." ) )
        self.personalNote = line[ 7 ]
        
        
