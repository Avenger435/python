"""
Practice module for Python string manipulation exercises.

This package contains various string processing utilities including:
- Special character removal
- Frequency counting
- Number removal
- Case conversion
- ASCII conversion
"""

__version__ = "1.0.0"
__author__ = "Python Learner"

# Import commonly used classes from all modules
from .remove_special_chars import Solution as StringCleaner
from .frequency_counter import Solution as FrequencyCounter
from .remove_nums_from_string import Solution as NumberRemover
from .replace_caps_to_smalls import Solution as CaseConverter
from .replace_chars_with_ascii_code import Solution as ASCIITransformer

__all__ = [
    "StringCleaner",
    "FrequencyCounter",
    "NumberRemover",
    "CaseConverter",
    "ASCIITransformer"
]
