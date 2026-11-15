import yaml
from pathlib import Path
from typing import Any, override
import shutil
from src.io_manager.io_static import IOStatic
from src.logger.logger import AppLogger
from src.note.note import Note

class IOManager( IOStatic ):

    def __init__(self, db_path: str | Path , output_folder : str | Path , autoclear_output : bool ):
        self.db_path = IOManager._get_path(db_path)
        self.output_folder = IOManager._get_path( output_folder )
        self.autocelar_output = autoclear_output 
        self.logger = AppLogger.get_logger( )

    def initalize_files( self ) :

        if self.autocelar_output :
            IOStatic.clear_folder_from( self.output_folder , ".yaml" )
        
        if self.output_folder.exists() :
            shutil.rmtree( self.output_folder )
    
        self.output_folder.mkdir(parents=True)

        if self.db_path.exists():
            self.logger.debug( f"Removing { self.db_path }")
            self.db_path.unlink()

    @override
    def get_notes_in_output_folder( self ):
        files = super().get_files_in_folder( self.output_folder )
        notes = list( )
        for file in files :
            if file.suffix == ".yaml" :
                self.logger.debug( f"Found note file { file }" )    
                notes.append( Note.from_yaml( file ) ) 

        return notes

    
    def save_notes( self , notes : list ) -> int:
        """Dump each note returned by a query into a separate YAML file."""
        if self.autocelar_output :
            IOStatic.clear_folder_from( self.output_folder , ".yaml" )

        for note in notes :

            if not( isinstance( note , Note ) ) :
                self.logger.warning( f"Unable to save as note { note } since is of type { type( note ) }" )
                continue 

            title_mod = note.title.replace( " " , "_" )
            note.to_yaml( self.output_folder / f"{note.note_id}_{ title_mod }.yaml")