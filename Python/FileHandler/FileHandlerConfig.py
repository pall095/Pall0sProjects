from enum import Enum

class ValidExtensions(Enum):
    EXCEL = "xlsx"
    CSV = "csv"
    YAML = "yaml"
    JSON = "json" 

    @classmethod
    def values(cls):
        return [ e.value for e in cls]