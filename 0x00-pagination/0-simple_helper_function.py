#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    Args:
         page, page_size
    Return:
          A tuple of size two (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    container = (start_index, end_index)  # return a tuple of size two
    return (container)
