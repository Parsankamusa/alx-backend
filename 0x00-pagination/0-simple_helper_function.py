#!/usr/bin/env python3
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Range of the page

    Args:
        page: Current page
        page_size: Total size of the page

    Return:
        Tuple with the range start and end size page
    """
    start_size = (page - 1) * page_size
    final_size = start_size + page_size

    return (start_size, final_size)
