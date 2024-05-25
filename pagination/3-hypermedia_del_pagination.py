#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()

            self.__indexed_dataset = {
                i: row for i, row in enumerate(dataset)
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        returns a dictonary of key-value pairs
        """
        assert type(index) == int or index is None
        assert type(page_size) == int and page_size > 0

        dataset = self.indexed_dataset()
        assert 0 <= index < len(dataset)

        data = []
        next_index = index
        for _ in range(page_size):
            while next_index not in dataset.keys():
                next_index += 1
            data.append(dataset[next_index])
            next_index += 1
  
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
