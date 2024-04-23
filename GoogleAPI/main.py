from utils import getValues 
from Entry import Entry



values = getValues() 
entriesList = [ ]


for item in values : 
    
    currentEntry = Entry( item )
    currentEntry.printEntry( )
    entriesList.append( currentEntry )
    