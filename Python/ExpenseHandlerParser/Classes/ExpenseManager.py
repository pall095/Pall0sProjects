from typing import override
import pandas as pd
from Classes.FileHandler import FileHandler 
from Classes.ManagerConfig import FrameColumns , OriginatorType
from Classes.FinancialEntry import FinancialEntry 
from Classes.FinancialEntryConfig import EntryType
from Classes.Categorizer import Categorizer 


class ExpenseManager :

    @staticmethod
    def check_columns( frame : pd.DataFrame ) :
        frame_cols = frame.columns.values.tolist( )
        for mandatory_col in FrameColumns.mandatory_as_list( ) :
            if not( mandatory_col in frame_cols ) :
                return False 
        return True
    


    
    @staticmethod
    def from_originator_list( originator_list : list[ tuple( OriginatorType , pd.DataFrame ) ] ) : # type: ignore
        manager = ExpenseManager( )

        if not( isinstance( originator_list , list ) ) :
            raise TypeError( "originator_list must be a list" )
        
        for tpl in originator_list  :
            if not( isinstance( tpl , tuple ) ) :
                raise TypeError( "All elements of the list must be tuples" )
            
            originator = tpl[ 0 ]
            frame = tpl[ 1 ]

            if not( isinstance( originator , OriginatorType ) ) :
                raise TypeError( "All elements first elements of the tuple must be OriginatorType" )

            if not( isinstance( frame , pd.DataFrame ) ) :
                raise TypeError( "All elements first elements of the tuple must be pd.DataFrame" )

            if not( ExpenseManager.check_columns( frame ) ) :
                raise AttributeError( f"The input data frame must contain the following columns: { FrameColumns.mandatory_as_list( ) }" )
        
        for tpl in originator_list  : 

            originator = tpl[ 0 ]
            frame = tpl[ 1 ]

            for row , row_content in frame.iterrows( ) :
                entry = FinancialEntry( 
                    row_content[ FrameColumns.DATE ] ,
                    row_content[ FrameColumns.AMOUNT ] ,
                    list( ) ,
                    row_content[ FrameColumns.DESCR ] ,
                    originator 
                )

                if entry.get_amount( ) != 0.0 :
                    manager.add_entry( entry )

        return manager 

    def __init__( self ) :
        self.entries_list = list( )

    def add_entry( self , e : FinancialEntry ) :
        self.entries_list.append( e ) 

    def get_metrics_string( self ) :

        first_entry = self.entries_list[ 0 ] 
        last_entry = self.entries_list[ 0 ] 
        total_in = 0 
        total_out = 0 

        for entry in self.entries_list :
            
            if entry.get_type( ) is  EntryType.INCOME :
                total_in += entry.get_amount( )
            
            if entry.get_type( ) is EntryType.EXPENSE :
                total_out += entry.get_amount( )
            
            if entry.is_before( first_entry ) :
                first_entry = entry 
            if entry.is_after( last_entry ) :
                last_entry = entry
        
        s = ""
        s = s + f"First day : { first_entry.get_date( ) }\n"
        s = s + f"Last day : { last_entry.get_date( ) }\n"
        s = s + f"Total In : { round( total_in , 2 ) }\n"
        s = s + f"Total Out : { round( total_out , 2 ) }\n"
        s = s + "\n"
        for label , label_dict in self.get_metrics_per_label( ).items( ) :
            s = s + f"Label : { label }\n\tCount : { label_dict[ "count" ] }\n\tAmount : { round( label_dict[ "amount" ] , 2 ) }\n\n"
        
        return s 
    

    def categorize_with( self , cat_instance : Categorizer ) :
        for entry in self.entries_list :
            labels = cat_instance.find_labels_new( entry )
            entry.add_labels( labels )

    def get_unique_labels( self ) :
        label_set = set( )
        for entry in self.entries_list :
            label_set.update( entry.get_labels( ) ) 
        return label_set

    def get_metrics_per_label( self ) :
        metrics_dict = dict( )
        for label in self.get_unique_labels( ) :
            metrics_dict[ label ] = dict( )
            metrics_dict[ label ][ "count" ] = 0
            metrics_dict[ label ][ "amount" ] = 0 

        for entry in self.entries_list :
            for entry_label in entry.get_labels( ) :
                metrics_dict[ entry_label ][ "count" ] += 1
                metrics_dict[ entry_label ][ "amount" ] += entry.get_amount( ) 
        
        return metrics_dict

    def get_entries( self , output_format = None ) :
        if output_format is None :
            return self.entries_list 
        elif output_format == pd.DataFrame :
            return pd.DataFrame( [ entry.as_dict( ) for entry in self.entries_list ] )
        else :
            raise ValueError( f"The specified output format { output_format } is unknown" )

    @override
    def __str__( self ) :
        for entry in self.entries_list :
            print( entry )