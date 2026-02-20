from datetime import date , datetime
from typing import override 
from dateutil import parser
from Classes.FinancialEntryConfig import EntryType
from Classes.ManagerConfig import OriginatorType


class FinancialEntry :

    def __init__(
        self,
        date_value: date | str,
        amount: float,
        labels: list[str],
        description: str,
        specific_type : str , 
        originator : OriginatorType 
    ):
        
        if isinstance(date_value, str):
            self.date = parser.parse(date_value, dayfirst=True).date()
        elif isinstance(date_value, date):
            self.date = date_value
        else:
            raise TypeError("Unsupported date type")


        self.amount = round( amount , 2 ) 

        if self.amount > 0.0 :
            self.type = EntryType.INCOME
        else :
            self.type = EntryType.EXPENSE

        self.specific_type = specific_type 
        self.labels = labels
        self.description = description
        self.originator = originator 

    
    def reset_labels( self , new_labels : list ) :
        if not( isinstance( new_labels , list ) ) :
            raise AttributeError( "new labels must be a list" )
        self.labels = new_labels 

    def get_type( self ) :
        return self.type 
    
    def get_originator( self ) :
        return self.originator 

    def get_date( self ) :
        return self.date 
    
    def get_amount( self ) :
        return self.amount 
    
    def get_labels( self ) :
        return self.labels 

    def add_labels( self , new_labels : list ) :
        self.labels.extend( new_labels ) 
    
    def get_description( self ) :
        return self.description 
    
    def compare_date( self , other_entry : FinancialEntry ) :
        delta = self.date - other_entry.get_date( ) 
        return delta.days 
    
    def as_dict( self , ) :
        return {
            "Originator" : self.originator ,
            "Type" : self.type , 
            "Specific Type" : self.specific_type , 
            "Date" : self.date ,
            "Amount" : self.amount ,
            "Description" :  self.description ,
            "Labels": self.labels  ,
        }

    @override
    def __str__( self ) :
        s = f"""
                Originator: { self.originator }\n   
                Specific Type : { self.specific_type }\n 
                Type: { self.type }\n 
                Date : { self.date }\n
                Amount : { self.amount }\n
                Description : { self.description}\n
                Labels:\n"""
        for l in self.labels :
            s = s + l + "\n"
        return s 

    