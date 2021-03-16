#!/usr/bin/env python3
""" Duck type an iterable object """

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Annotated function """
    return [(i, len(i)) for i in lst]
