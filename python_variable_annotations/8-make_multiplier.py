#!/usr/bin/env python3
"""
Make Multiplier file
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a function
    that multiplies a value by the given multiplier.

    Args:
    - multiplier (float):
        The multiplier value to be stored in the created function.

    Returns:
    - Callable[[float], float]:
         A function that accepts a float value and returns the
         result of multiplying that value by the stored multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiply a value by the stored multiplier.

        Args:
        - x (float): The value to be multiplied.

        Returns:
        - float: The result of multiplying the value by the stored multiplier.
        """
        return x * multiplier

    return multiplier_function
