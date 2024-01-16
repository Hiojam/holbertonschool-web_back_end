#!/usr/bin/env python3
"""
Task 0: Simple Helper Function
"""


def index_range(page, page_size) -> tuple:
    """
    Calculate the start and end indices for a given page and page size.

    Parameters:
    - page (int): The page number.
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start and end indices.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
