from Classes.FinancialEntry import FinancialEntry 
import re


class Categorizer :

    @staticmethod
    def from_dict( categories_dict : dict ) :
        cat = Categorizer( )
        cat.set_categories( categories_dict )
        return cat 

    def __init__( self ) :
        self.categories_dict = dict( )

    def set_categories( self , categories_dict : dict ) :
        self.categories_dict = categories_dict 

    
    def find_labels( self , entry : FinancialEntry ) :
        exact_set = self.find_labels_by_exact_match( entry )
        subsstring_set = self.find_labels_by_substring( entry.get_description() ) 
        final = exact_set + subsstring_set 
        if len( final ) == 0 :
            return [ "Generic" ] 
        else :
            return list( set( final ) ) 

    def find_labels_by_substring(self, entry_descr: str):
        matching_labels = []

        for label, matching_descriptions in self.categories_dict.items():
            for pattern in matching_descriptions:
                if re.search(pattern, entry_descr, re.IGNORECASE):
                    matching_labels.append(label)

        return list(set(matching_labels))


    def find_labels_by_exact_match( self , entry : FinancialEntry ) :
        matching_labels = list( )
        for label , matching_descriptions in self.categories_dict.items( ) :
            for match_desc in matching_descriptions :
                if match_desc == entry.get_description( ) :
                    matching_labels.append( label )
        
        return list( set( matching_labels ) ) 
