#!/usr/bin/python3
"""TMethod that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    # Initialize a variable to keep
    # track of the number of bytes expected
    bytes_to_follow = 0

    for byte in data:
        # Check if the byte is a continuation byte
        # (has the format 10xxxxxx)
        if 0b10000000 <= byte <= 0b10111111:
            # If it's not a valid continuation byte, return False
            if bytes_to_follow == 0:
                return False
            bytes_to_follow -= 1
        else:
            if bytes_to_follow > 0:
                return False
            # Determine the number of bytes to follow based on the
            # first few bits of the byte
            if byte & 0b10000000 == 0:
                bytes_to_follow = 0
            elif byte & 0b11100000 == 0b11000000:
                bytes_to_follow = 1
            elif byte & 0b11110000 == 0b11100000:
                bytes_to_follow = 2
            elif byte & 0b11111000 == 0b11110000:
                bytes_to_follow = 3
            else:
                return False

    # If there are still bytes to follow,
    # it's an incomplete sequence
    return bytes_to_follow == 0
