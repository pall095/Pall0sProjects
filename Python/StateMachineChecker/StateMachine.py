from State import State
from Transition import Transition 
import json
from colorama import Fore , init

class StateMachine :

    @classmethod
    def allocate_from_json( cls , filename ) :
        
        obj = cls( )
        with open( filename , "r" ) as json_file :
            definition_list = json.load( json_file ) 
        
        for state_dict in definition_list :
            obj.state_list.append( State.allocate_from_dict( state_dict ) ) 

        obj.set_state( obj.state_list[ 0 ] )
    
        return obj


    def __init__(self):
        # Initializes Fore
        init( autoreset = True )

        # Initialzies attributes
        self.state_list = list( )
        self.input_sequence = list( )
        self.curret_state = State( )
        self.is_running = False
        self.match_count = 0 
        self.time = 0 

    # Loop function 
    def run( self ) :

        self.is_running = True 

        while self.is_running :
            self.print_status( )
            self.process_input( )

    # Evaluates which state to go based on current input.
    def eval( self , current_input ) :
        
        # Find the transition that verifies the input and sets the current state
        for transition in self.curret_state.transitions_list :
            if transition.trigger == current_input :
                self.set_state( transition.destination )
                return

        print( Fore.RED + "Current input does not lead to any state!" ) 
        return 
    
    # Updates count if output is equal to 1
    def update_count( self ) :
        if self.curret_state.output == 1 :
            self.match_count += 1 

    def process_input( self ) :

        current_input = int( input( "Provide input:" ) )
        self.input_sequence.append( current_input )

        if current_input == -1 :
            self.is_running = False 
        else :
            self.eval( current_input )

        self.time += 1 
        return



        
        
    # SETTERS 
    # Sets the current state.
    # State request can either be a string (plain state name) or a State object
    def set_state( self , state_req ) :
        if type( state_req ) is State :
            self.set_state_by_state( state_req )
        elif type( state_req ) is str :
            self.set_state_by_name( state_req )
        else :
            raise AttributeError( "The state argument to \"set_state\" must be of typ \"str\" or \"Stat\"")
        
        self.update_count( )
        
    def set_state_by_state( self , state_req : State ) :
        for state in self.state_list :
            if state.name == state_req.name :
                self.curret_state = state 
                return
        raise KeyError( f"State { state_req.name } was not found in the list of available states")

            
    def set_state_by_name( self , state_req : str ) :
        for state in self.state_list :
            if state.name == state_req :
                self.curret_state = state
                return
        raise KeyError( f"State { state_req } was not found in the list of available states")

                 

    # UTILS #
    def print_state_machine( self ) :
        for state in self.state_list :
            state.print_state( )

    def print_status( self ) :
        print( Fore.GREEN + "-----------" )
        self.print_current_time( )
        self.print_match_count( )
        self.print_input_sequence( )
        self.print_current_state( )
        print( Fore.GREEN + "-----------" )

    def print_current_state( self ) :
        print( Fore.GREEN + "Current State : " , )
        self.curret_state.print_state( indent = 1 )

    def print_current_time( self ) :
        print( Fore.GREEN + f"Current Time : { self.time }")
    
    def print_match_count( self ) :
        print( Fore.GREEN + f"Match Count : { self.match_count }")

    def print_input_sequence( self ) :
        print( Fore.GREEN + "Input sequence : " , end = "" )
        for value in self.input_sequence :
            print( Fore.GREEN + f" { value }" , end = "" )
        
        print( )
