from enum import Enum
from typing import Dict, List
from pydantic import BaseModel, RootModel, model_validator
from Classes.FinancialEntryConfig import EntryType


# ---------- ENUM ----------
class RuleType(str, Enum):
    EXACT = "exact"
    REGEX = "regex"
    SUBSTRING = "substring"
    DEFAULT = "default"


# ---------- MODEL ----------
class Rule(BaseModel):
    type: RuleType
    content: str


# ---------- ROOT MODEL ----------
class Ruleset(RootModel[Dict[str, List[Rule]]]):

    # --- validation ---
    @model_validator(mode="after")
    def validate_defaults(self):
        defaults = []
        contents = set()

        # single pass, no intermediate allocations
        for rules in self.root.values():
            for rule in rules:
                if rule.type == RuleType.DEFAULT:
                    defaults.append(rule)
                    contents.add(rule.content)

        if len(defaults) != 2:
            raise ValueError(
                "Ruleset must contain exactly two DEFAULT rules"
            )

        if contents != { EntryType.EXPENSE.value , EntryType.INCOME.value }:
            raise ValueError(
                f"DEFAULT rules must have content { EntryType.EXPENSE.value } and { EntryType.INCOME.value }"
            )

        return self

    # --- helpers ---
    @property
    def default_rules(self) -> List[Rule]:
        return [
            rule
            for rules in self.root.values()
            for rule in rules
            if rule.type == RuleType.DEFAULT
        ]

    @property
    def defaults_map(self) -> Dict[str, Rule]:
        return {r.content: r for r in self.default_rules}
    
    def get_default_category(self, name: str) -> str:
        for category, rules in self.root.items():
            for rule in rules:
                if rule.type == RuleType.DEFAULT and rule.content == name:
                    return category

        raise KeyError(f"No default '{name}' found")

