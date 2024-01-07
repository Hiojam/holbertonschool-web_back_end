#!/usr/bin/env python3
"""7"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key-value pair into a tuple where the value is squared.

    Args:
    - k (str): A string representing the key.
    - v (Union[int, float]): An integer or float representing the value.

    Returns:
    - Tuple[str, float]:
         A tuple containing the original key and the squared value.
    """
    return (k, v**2)
