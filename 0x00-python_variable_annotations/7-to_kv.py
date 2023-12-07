#!/usr/bin/env python3
"""
type-annotated function
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of (k, v^2)"""
    return (k, v**2)
