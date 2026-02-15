from Classes.FileHandler import FileHandler 
from Classes.ExpenseManager import ExpenseManager
from Classes.Categorizer import Categorizer 
import pandas as pd
 
frames_to_process = list( )
input_couples = [
    ( "revolut.csv" , "RevolutMapper.json" ) ,
    ( "Azzoaglio.csv" , "AzzoaglioMapper.json" )
]

for couple in input_couples : 
    cf = FileHandler.remap_columns( FileHandler.read_csv( couple[ 0 ] ) , FileHandler.read_json( couple[ 1 ] ) )
    frames_to_process.append( cf )

manager = ExpenseManager.from_frames( frames_to_process )
manager.categorize_with( Categorizer.from_dict( FileHandler.read_yaml( "categories.yaml" ) ) )
FileHandler.frame_to_csv( manager.get_entries( output_format = pd.DataFrame ) , "prova_out.csv" )
FileHandler.string_to_txt( manager.get_metrics_string( ) , "metriche.txt" )  

 

