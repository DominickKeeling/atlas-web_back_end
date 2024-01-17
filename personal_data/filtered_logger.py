#!/usr/bin/env python3

""" Write a function called filter_datum that returns the log message obfuscated """

import re
import logging
from typing import List
import os
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str],
                   redaction: str,
                   message: str,
                   separator: str) -> str:
    """ returns log message """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ method to filter values in incoming log records """
        original_formatted_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original_formatted_message, self.SEPARATOR)

def get_logger() -> logging.Logger:
    """ Takes no arguments and returns a logging.Logger object """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connections.MySQLConnection:
    """ fetch datanase credentials from env variables with default vals """
    db_user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME') 
    return mysql.connector.connect(user=db_user,
                                password=db_password,
                                host=db_host,
                                database=db_name)


def main():
    """ Main function """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")
    for row in cursor:
        print(row[0])
    cursor.close()
    db.close()

if __name__ == '__main__':
    main()