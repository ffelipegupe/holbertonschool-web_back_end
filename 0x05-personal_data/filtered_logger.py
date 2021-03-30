#!/usr/bin/env 
""" Regex-ing """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str)-> str:
    """ Function that returns the log message obfuscated """
    for f in fields:
        message = re.sub(fr"{f}=.+?{separator}",
                         f'{f}={redaction}{separator}', message)
    return message
