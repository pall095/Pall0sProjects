from enum import Enum
from pydantic import BaseModel , RootModel
from typing import Dict, List


class FrameColumns(str, Enum):
    DATE = "Date"
    AMOUNT = "Amount" 
    LABELS = "labels"
    DESCR = "Description"

    @classmethod
    def mandatory_as_list(cls) -> list[str]:
        return [ cls.AMOUNT.value , 
                cls.DATE.value , 
                cls.DESCR.value ]
    

class OriginatorType(str, Enum):
    REVOLUT = "Revolut"
    AZZOAGLIO = "Azzoaglio"


