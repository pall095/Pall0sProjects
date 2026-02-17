from enum import Enum

class EntryType(str, Enum):
    EXPENSE = "expense"
    INCOME = "income"
