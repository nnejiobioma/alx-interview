#!/usr/bin/python3
"""Lockboxes task solved"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = set()  # To keep track of visited boxes
    stack = [0]  # Start with the first box (box 0)

    while stack:
        current_box = stack.pop()
        visited.add(current_box)

        # Check all keys in the current box
        for key in boxes[current_box]:
            if key >= 0 and key < n and key not in visited:
                stack.append(key)

    # If all boxes have been visited, return True
    return len(visited) == n
