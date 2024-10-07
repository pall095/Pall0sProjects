from utils import getValues 
from Entry import Entry
from EntriesDatabase import EntriesDatabase
import gkeepapi


grab_max = 10000
values = getValues( grab_max ) 

dbHandler = EntriesDatabase( ) 

new_entry_amount = 10
new_entry_date = "30 Apr 2024"
new_entry_descr = "tette"



for item in values : 
    
    # Checking if the first element is empty
    # TO DO: is there a better method? If you check if the list is empty it return false because you always have the month at the end.
    if item[ 0 ] != "" :

        current_entry = Entry( item )
        dbHandler.addParsedEntry( current_entry )
    
        
#dbHandler.addUnparsedentry(new_entry_date, new_entry_descr, new_entry_amount)



