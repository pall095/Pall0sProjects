

class Transition :

    DESTINATION_KEY = "Destination"
    TRIGGER_KEY = "Trigger"

    @classmethod
    def allocate_from_dict( cls , definition_dict : dict ) :
        obj = cls( )
        obj.destination = definition_dict[ Transition.DESTINATION_KEY ] 
        obj.trigger = definition_dict[ Transition.TRIGGER_KEY ]
        return obj

    def __init__( self ) :
        self.destination = "Null"
        self.trigger = bool( )
        return

    def print_transition( self ) -> None :
        print( f"Destination : { self.destination } - Trigger : { self.trigger }" ) 
        return 
