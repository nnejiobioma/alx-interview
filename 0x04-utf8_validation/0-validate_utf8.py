#!/usr/bin/python3
"""TMethod that determines if a given data set
represents a valid UTF-8 encoding.
"""


def get_leading_set_bits(num):
    """Return:
True if data is a valid UTF-8 encoding,
else return False
"""
    bits = 0
    helper = 1 << 7
    while helper & num:
        bits += 1
        helper = helper >> 1
    return bits


def validUTF8(data):
    """ This is set to gets if a given data set
represents a valid UTF-8 encoding
"""
    count = 0
    for i in range(len(data)):
        if count == 0:
            count = get_leading_bits(data[i])
            '''1-byte (format: 0xxxxxxx)'''
            if count == 0:
                continue
            '''UTF-8 character this can be 1 to 4 bytes long'''
            if count == 1 or count > 4:
                return False
        else:
            '''checks current byte format 10xxxxxx'''
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        count -= 1
    return count == 0
