#!/usr/bin/env python3
"""
9
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing sequences and their respective lengths.

    Args:
    - lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
    - List[Tuple[Sequence, int]]:
         A list of tuples where each tuple contains a sequence
         from the input and its corresponding length.
    """
    result = []

    for i in lst:
        result.append((i, len(i)))
    return result
