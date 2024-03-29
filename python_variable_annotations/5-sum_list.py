#!/usr/bin/env python3
"""
Sum list file
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): The input list of floats.

    Returns:
        float: The sum of all floats in the input list.
    """
    return sum(input_list)
