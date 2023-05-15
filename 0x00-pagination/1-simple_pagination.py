#!/usr/bin/env python3
import csv
from math import ceil
from typing import List, Tuple, Dict


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = list(reader)[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        dataset = self.dataset()

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}

        dataset = self.dataset()
        total_pages = ceil(len(dataset) / page_size)
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        hypermedia = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return hypermedia


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
