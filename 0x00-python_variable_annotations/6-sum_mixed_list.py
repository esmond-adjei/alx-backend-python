#!/usr/bin/env python3
"""
type-annotated function
"""
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """sums list values"""
    return sum(mxd_lst)
