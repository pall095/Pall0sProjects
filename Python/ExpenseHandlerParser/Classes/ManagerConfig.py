from enum import Enum

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
    
