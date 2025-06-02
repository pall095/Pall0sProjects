from Transition import Transition

class State :

    NAME_KEY = "Name"
    TRANSITION_KEY = "Transitions"
    OUTPUT_KEY = "Output"

    @classmethod
    def allocate_from_dict( cls , definition_dict : dict ) :
        obj = cls( )
        obj.name= definition_dict[ State.NAME_KEY ] 
        obj.output = definition_dict[ State.OUTPUT_KEY ]
        transition_list = definition_dict[ State.TRANSITION_KEY ]

        for transition_dict in transition_list :
            obj.transitions_list.append( Transition.allocate_from_dict( transition_dict ) ) 

        return obj

    def __init__( self ) :
        self.name = "NULL"
        self.output = "NULL"
        self.transitions_list = list( )
    

    def get_name( self ) :
        return self.name 

    def print_state( self , indent : int = 0 ) :
        print( "\t" * indent + f"Name : { self.name } - Output : { self.output }" )
        print( "\t" * indent + f"Transitions : " )
        for num , transition in enumerate( self.transitions_list ) :
            print( "\t" * indent + f"{ num }) " , end = "" )
            transition.print_transition( )






