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

    