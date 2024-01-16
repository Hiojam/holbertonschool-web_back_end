#!/usr/bin/env python3
"""
Task 1: Simple Helper Functions for Paginating Popular Baby Names
"""

import csv
import math
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieve paginated baby name data with hypermedia information.

        Parameters:
        - page (int): The page number.
        - page_size (int): The number of items per page.

        Returns:
        - dict: A dictionary containing hypermedia information
          along with baby name data.
        """
        metadata = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(metadata),
            'page': page,
            'data': metadata,
            'next_page': page + 1 if page + 1 < total_pages else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_pages': total_pages
        }


def index_range(page, page_size) -> tuple:
    """
    Calculate the start and end indices for a given page and page size.
    """
    return (page * page_size) - page_size, page * page_size
