from datetime import date , datetime
from typing import override 
from dateutil import parser


class FinancialEntry :

    def __init__(
        self,
        date_value: date | str,
        amount: float,
        labels: list[str],
        description: str,
    ):

        if isinstance(date_value, str):
            self.date = parser.parse(date_value, dayfirst=True).date()
        elif isinstance(date_value, date):
            self.date = date_value
        else:
            raise TypeError("Unsupported date type")


        self.amount = round( amount , 2 ) 
        self.labels = labels
        self.description = description

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
    
    def is_before(self, other_entry: "FinancialEntry") -> bool:
        return self.date < other_entry.get_date()

    def is_after(self, other_entry: "FinancialEntry") -> bool:
        return self.date > other_entry.get_date()


    @override
    def __str__( self ) :
        s = f"Date : { self.date } - Amount : { self.amount } - Description : { self.description} \n"
        s = s + "Labels:\n"
        for l in self.labels :
            s = s + l + "\n" 
        return s 

    