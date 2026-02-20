from Classes.FileHandler import FileHandler 
from Classes.ExpenseManager import ExpenseManager
from Classes.Categorizer import Categorizer 
from Classes.ManagerConfig import OriginatorType 
import pandas as pd
 
CATEGORIZER_FILE = r"InputFIles\new_categories.yaml"

REVOLUT_MAPPER = r"InputFiles\RevolutMapper.json"
REVOLUT_IN = r"InputFiles\revolut.csv"

AZZOAGLIO_MAPPER = r"InputFiles\AzzoaglioMapper.json"
AZZOAGLIO_IN = r"InputFiles\Azzoaglio.csv"

input_triplet = [
        ( REVOLUT_IN , REVOLUT_MAPPER , OriginatorType.REVOLUT ) ,
        ( AZZOAGLIO_IN , AZZOAGLIO_MAPPER , OriginatorType.AZZOAGLIO )
    ]


originator_list = list(  )

for triplet in input_triplet : 
    cf = FileHandler.remap_columns( FileHandler.read_csv( triplet[ 0 ] ) , FileHandler.read_json( triplet[ 1 ] ) )
    originator_list.append(
        ( triplet[ 2 ] , cf )
    )

manager = ExpenseManager.from_originator_list( originator_list  )
cat = Categorizer.from_dict( FileHandler.read_yaml( CATEGORIZER_FILE ) )
manager.categorize_with( cat )
cat.annihilate_expenses( manager.get_incomes( ) , manager.get_expenses( ) , verbose = False ) 
FileHandler.frame_to_excel( manager.get_entries( output_format = pd.DataFrame ) , "data_out.xlsx" , sheet_name = "Data" ) 

 

