import pandas as pd

class DbManager :

    def __init__( self , db_path ) :
        self.db_path = db_path
        self.load( )

    def load( self ) :
        self.db_frame = pd.read_csv( self.db_path ) 

    def write( self ) :
        self.db_frame.to_csv( self.db_path , index = False ) 

    def append_entry(self, entry: dict):
        self.db_frame = pd.concat(
            [self.db_frame, pd.DataFrame([entry])],
            ignore_index=True
        )

    def cancel_entry(self, date, entry_type, source):
        self.db_frame = self.db_frame[
            ~(
                (self.db_frame["date"] == str(date))
                & (self.db_frame["type"] == entry_type)
                & (self.db_frame["source"] == source)
            )
        ].reset_index(drop=True)

        self.write()