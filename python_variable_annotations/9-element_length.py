#!/usr/bin/env python3
"""9-element_length.py
"""
def element_length(lst: list) -> list:
    """Returns a list of the lengths of the elements of a list
    Args:
        lst (list): list of strings to get the length of
    Returns:
        list: a list of the lengths of the elements of lst
    """
    return [len(i) for i in lst]
