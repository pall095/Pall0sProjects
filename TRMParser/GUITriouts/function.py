class Function:

    def __init__(self , phys , sysElement , PID , functionName ):

        self.name = functionName
        self.pid = PID
        self.syselement = sysElement
        self.phys = phys
        self.reqlist = [ ]
        self.numInWork = 0
        self.numFrozen = 0
        self.numReleased = 0




    def getName( self ):
        return self.name
    def setName( self , newName ):
        self.name = newName

    def getPid( self ):
        return self.pid
    def setName( self , newPid ):
        self.pid = newPid

    def getSyselement( self ):
        return self.syselement
    def setName( self , newSyselement ):
        self.syselement = newSyselement

    def getPhys( self ):
        return self.phys
    def setName( self , newPhys ):
        self.phys = newPhys

    def getReqlist( self ):
        return self.reqlist
    def appendReq( self , req ):
        self.reqlist.append( req )

    def getNumInWork( self ):
        return self.numInWork
    def setNumInWork( self , num ):
        self.numInWork = num
    def increseNumInWork( self ):
        self.numInWork = self.numInWork + 1

    def getNumInFrozen( self ):
        return self.numFrozen
    def setNumFrozen( self , num ):
        self.numFrozen = num
    def increseFrozen( self ):
        self.numFrozen = self.numFrozen + 1

    def getNumReleased(self):
        return self.numReleased
    def setNumReleased(self, num):
        self.numReleased= num
    def increseReleased(self):
        self.numReleased = self.numReleased + 1






