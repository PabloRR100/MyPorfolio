"""
file: porfolio.py
description: Types and constants.
"""
from enum import Enum


class ExpandedEnum(Enum):
    @classmethod
    def all_values(cls):
        """Returns the list of all training statuses in model training."""
        type_values = []
        for type in cls:
            type_values.append(type.value)
        return type_values

    @classmethod
    def from_string(cls, string):
        """Obtains the internal enum representation from a constant string."""
        for enum_type in cls:
            if enum_type.value == string:
                return enum_type
        raise TypeError(f"{string} is not a valid {cls} value")

