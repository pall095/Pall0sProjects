from enum import Enum
from typing import Dict, List

from pydantic import BaseModel, RootModel, model_validator, Field

from Classes.FinancialEntryConfig import EntryType


# ---------- ENUM ----------
class RuleType(str, Enum):
    EXACT = "exact"
    REGEX = "regex"
    SUBSTRING = "substring"
    DEFAULT = "default"


# ---------- RULE ----------
class Rule(BaseModel):
    type: RuleType
    content: str


# ---------- CATEGORY WRAPPER ----------
class CategoryConfig(BaseModel):
    annihilable: bool = False
    rules: List[Rule] = Field(default_factory=list)


# ---------- ROOT MODEL ----------
class Ruleset(RootModel[Dict[str, CategoryConfig]]):

    # ==========================================================
    # VALIDATION (unchanged logic, adapted to new structure)
    # ==========================================================
    @model_validator(mode="after")
    def validate_defaults(self):

        defaults = []
        contents = set()

        for category in self.root.values():
            for rule in category.rules:
                if rule.type == RuleType.DEFAULT:
                    defaults.append(rule)
                    contents.add(rule.content)

        if len(defaults) != 2:
            raise ValueError(
                "Ruleset must contain exactly two DEFAULT rules"
            )

        if contents != {
            EntryType.EXPENSE.value,
            EntryType.INCOME.value,
        }:
            raise ValueError(
                f"DEFAULT rules must have content "
                f"{EntryType.EXPENSE.value} and {EntryType.INCOME.value}"
            )

        return self

    # ==========================================================
    # HELPERS
    # ==========================================================
    @property
    def default_rules(self) -> List[Rule]:
        return [
            rule
            for category in self.root.values()
            for rule in category.rules
            if rule.type == RuleType.DEFAULT
        ]

    @property
    def defaults_map(self) -> Dict[str, Rule]:
        return {r.content: r for r in self.default_rules}

    def get_default_category(self, name: str) -> str:
        for category_name, category in self.root.items():
            for rule in category.rules:
                if rule.type == RuleType.DEFAULT and rule.content == name:
                    return category_name

        raise KeyError(f"No default '{name}' found")

    # ==========================================================
    # NEW FEATURE
    # ==========================================================
    def get_annihilable_categories(self) -> List[str]:
        """
        Returns all category names that have annihilable=True
        """
        return [
            name
            for name, category in self.root.items()
            if category.annihilable
        ]