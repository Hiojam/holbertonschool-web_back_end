#!/usr/bin/env python3
"""
Task 1: Simple Helper Function for Paginating Popular Baby Names
"""

import csv
from typing import List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specified page of popular baby names.

        Parameters:
        - page (int): The page number.
        - page_size (int): The number of items per page.

        Returns:
        - List[List]: A list containing baby name data for the specified page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        index_set = index_range(page, page_size)
        first = index_set[0]
        last = index_set[1]
        return self.dataset()[first:last]


def index_range(page, page_size) -> tuple:
    """
    Calculate the start and end indices for a given page and page size.
    """
    return (page * page_size) - page_size, page * page_size
