import pandas as pd
from RequirementManager_2 import RequirementManager




PATH_DELIMITER = "\\"

requirement_manager = RequirementManager.from_data_frame( pd.read_csv( "requirements.csv") , path_delimiter = "\\" )