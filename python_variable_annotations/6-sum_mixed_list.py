#!/usr/bin/env python3
"""
6
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing mixed integer and float elements.

    Args:
    - mxd_lst (List[Union[int, float]]):
         A list containing integer and/or float elements.

    Returns:
    - float: The sum of all elements in the input list.
    """
    return sum(mxd_lst)
