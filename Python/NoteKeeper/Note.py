import datetime

class Note :
	
	def __init__( self , text , date : datetime.date , is_meeting, is_todo , deadline : datetime.date , tags : list ) :
		self.text = text
		self.tags = tags 
		self.date = date 
		self.is_meeting = is_meeting
		self.is_todo = is_todo
		self.deadline = deadline 

	def print_note( self ) :
		print( f"Content : { self.text }" )
		print( f"Date : { self.date }" )
		print( f"Is from meeting : { self.is_meeting }" )
		print( f"Is to do : { self.is_todo }" )
		print( f"Deadline : { self.deadline }" ) 
		print( f"Tags : { self.tags }" )

	def print_note( self , new_line_char = "\n" ) :
		print( f"Insertion Date : { self.date } | Meeting Note : { self.is_meeting } | To Do : { self.is_todo } - Deadline : { self.deadline } | Tags : { self.tags } |" )
		print( f"Content : \n { self.text.replace( new_line_char , "\n" ) }" )
		print( "                                " )
	
	def to_list( self ) :
		return [ self.text , self.date , self.is_meeting , self.is_meeting , self.deadline , self.tags ]


