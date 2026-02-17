from Classes.FinancialEntry import FinancialEntry 
from Classes.CategorizerConfig import Ruleset , RuleType , Rule
import re


class Categorizer :

    @staticmethod
    def from_dict( rules_dict : dict ) :
        cat = Categorizer( )
        cat.set_rules( rules_dict )
        return cat 

    def __init__( self ) :
        self.categories_dict = dict( )

    def set_rules( self , rules_dict  : dict ) :
        self.ruleset = Ruleset( rules_dict ) 

    
    def find_labels_new( self , entry : FinancialEntry ) :
        label_set = set( )
        for category , rules in self.ruleset.root.items( ) :
            for rule in rules :
                if( self.match( entry.get_description( ) , rule ) ) :
                    label_set.add( category )

        if len( label_set ) == 0 :
            return set( [ "Generic" ] ) 
    
        return label_set 

    def match( self , entry_description : str , rule : Rule ) -> bool :
        if rule.type == RuleType.EXACT :
            return self.match_exact( entry_description , rule.content )
        elif rule.type == RuleType.SUBSTRING :
            return self.match_substring( entry_description , rule.content )
        elif rule.type == RuleType.REGEX :
            return self.match_regex( entry_description , rule.content )
        else :
            raise TypeError( "Invalid rule type!" )


    def match_exact( self , entry_description: str, rule_content: str) -> bool:
        """
        Version 1 — exact match.
        True only if the two strings are identical.
        """
        return entry_description == rule_content


    def match_substring( self , entry_description: str, rule_content: str) -> bool:
        """
        Version 2 — substring check.
        True if rule_content appears anywhere inside entry_description.
        No regex involved.
        """
        return rule_content in entry_description


    def match_regex( self , entry_description: str, rule_content: str) -> bool:
        """
        Version 3 — pure regex evaluation.
        No assumptions, no added anchors, no flags.
        If the regex matches anywhere, return True.
        """
        return re.search(rule_content, entry_description) is not None
