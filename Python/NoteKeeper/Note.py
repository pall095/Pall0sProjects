import datetime

class Note :
	
	def __init__( self , text , date : datetime.date , is_todo , tags : list ) :
		self.text = text
		self.tags = tags 
		self.date = date 
		self.is_todo = is_todo

	def print_note( self ) :
		print( f"Content : { self.text }" )
		print( f"Date : { self.date }" )
		print( f"Is to do : { self.is_todo }" )
		print( f"Tags : { self.tags }" )

	def print_note( self , new_line_char = "\n" ) :
		print( f"Insertion Date : { self.date } | To Do : { self.is_todo } - Tags : { self.tags } |" )
		print( f"Content : \n { self.text.replace( new_line_char , "\n" ) }" )
		print( "                                " )
	
	def to_list( self ) :
		return [ self.text , self.date , self.is_todo , self.tags ]


