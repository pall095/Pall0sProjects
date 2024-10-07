from Entries import Entry


if __name__ == "__main__" :
    
    f = "ExpenseHandler_V2_Uscite_tabbed.tsv"
    
    Entry.populateList( f )
    
    # List of categories and sub-categories. 
    # Every even index (0 , 2 , 4 ... ) is a category. Every odd index is a list of subcategories.
    catList = [ ]
    
    
    # Iterate over the entries list. Everytime if find a category and it is new, it gets appended to the list and an empty list is added to the index next to it and
    # immediately append the subcategory to that list (if the entry is new the subcat also is )
    # If the category is inside the list already, populates the subcat list with a similar logic (check if already present, if not gets appended to the correct subcat list )

    for item in Entry.entriesList :
        
        if item.cat not in catList :
            
            catList.append( item.cat )
            index = catList.index( item.cat ) + 1 
            catList.insert( index , [] )
            catList[ index ].append( item.subcat )
            
        if item.cat in catList :
            
            index = catList.index( item.cat ) + 1 
            
            if item.subcat not in catList[ index ]:
                catList[ index ].append( item.subcat )
            
    print( catList )
            
            
            
    
        
