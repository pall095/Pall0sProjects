from enum import Enum
from pydantic import BaseModel , RootModel
from typing import Dict, List

class RuleType(str, Enum):
    EXACT = "exact"
    REGEX = "regex"
    SUBSTRING = "substring"

class Rule(BaseModel):
    type: RuleType
    content: str

class Ruleset(RootModel[Dict[str, List[Rule]]]):
    pass
