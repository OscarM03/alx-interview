#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Valid utf-8 encoding"""
    for item in data:
        int_byte = item.to_bytes((item.bit_length() + 7) // 8, 'big')
        try:
            int_byte.decode('utf-8')
        except(UnicodeDecodeError):
            return False
    return True
