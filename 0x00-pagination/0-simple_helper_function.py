#!/usr/bin/env python3
"""Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """
    Return the start index and end index for a given pagination.
    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.
    Returns:
        tuple: A tuple containing the start index and
        end index for the given pagination.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
