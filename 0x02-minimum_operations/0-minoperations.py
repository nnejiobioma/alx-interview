def minOperations(z):
    '''
    This function calculates the minimum number of operations required to achieve 'z' characters.

    Args:
        z: Number of 'z' characters to be achieved.

    Returns:
        track_ops: Fewest number of operations required.
    '''
    if not isinstance(z, int) or z < 1:
        return 0

    track_ops = 0  # Tracks operations
    current_num = 1   # Initial characters
    clipboard = 0

    while current_num < z:
        if z - current_num >= current_num:
            # Copy all and paste
            clipboard = current_num
            current_num += clipboard
            track_ops += 2
        else:
            # Paste
            current_num += clipboard
            track_ops += 1

    return track_ops

# Example usage:
z = 10
operations = minOperations(z)
print(f"Minimum operations to achieve {z} characters: {operations}")
