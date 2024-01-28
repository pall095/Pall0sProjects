class Function:

    def __init__(self , phys , sysElement , PID , functionName ):

        self.name = functionName
        self.pid = PID
        self.syselement = sysElement
        self.phys = phys
        self.reqlist = [ ]



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

