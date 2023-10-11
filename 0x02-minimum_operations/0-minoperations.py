#!/usr/bin/python3
'''
Code Challange, Calculated minimum number of 
operations(track_ops) required
'''


def minOperations(z):
    '''
    This is the operations required to achieve z
    s characters. This returns fewest number of 
    operations

    Args:
        z: Number of s characters(chars_init)

    Return: Few number of operations(track_ops)
    '''
    if not isinstance(z, int):
        return 0
    track_ops = 0  # Tracks operations
    current_num = 0   # Stores number of characters
    chars_init = 1  # Initial characters

    while chars_init < z:
        if current_num == 0:
            #first copy all and paste resualt 
            current_num = chars_init
            chars_init += clipboard
            track_ops += 2

        elif z - chars_init > 0 and (z - chars_init) % chars_init == 0:
            # copy all and paste
            current_num = chars_init
            chars_init += current_num
            track_ops += 2

        elif clipboard > 0:
            # paste
            chars_init += current_num
            track_ops += 1

    return track_ops