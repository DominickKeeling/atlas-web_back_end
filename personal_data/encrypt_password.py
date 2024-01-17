#!/usr/bin/env python3

""" Implement a hash_password function that expects one string argument name
password and returns a salted, hashed password, which is a byte string
Use the bcrypt package to perform the hashing (with hashpw)
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ returns a salted hashed password """
    salt = bcrypt.gensalt()
    hashd_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashd_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks for valid password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
