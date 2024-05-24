#!/usr/bin/env python3

"""
Write a function called filter_datum that returns the log message obfuscated:

Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by which character is separating all fields in
the log line (message)
The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub to perform the
substitution with a single regex.
"""

import re
import logging
from typing import List


PII_FIELDS = ('name', 'email', 'ssn', 'password', 'phone')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    returns obfuscated message
    """
    looking_for = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(looking_for, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    """
    Update the class to accept a list of strings fields constructor argument.
    Implement the format method to filter values in incoming log records using
    filter_datum. Values for fields in fields should be filtered.
    DO NOT extrapolate FORMAT manually. The format method should be less than
    5 lines long.
    """

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values for incoming log records """
        original_formatted_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_formatted_message,
                            self.SEPARATOR)

def get_logger():
    """ retunds a logger object """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)
