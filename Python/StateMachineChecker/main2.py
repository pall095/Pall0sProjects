from StateMachine import StateMachine 
from tkinter import filedialog

state_machine_file = filedialog.askopenfilename( )
machine = StateMachine.allocate_from_json( state_machine_file )
machine.run( )