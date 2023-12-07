#!/usr/bin/env python3
"""
type-annotated function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sums list values"""
    return sum(mxd_lst)
