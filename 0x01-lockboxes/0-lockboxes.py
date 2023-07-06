#!/usr/bin/python3
'''Unlocking Boxes'''


def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    visited = set()  # Set to store visited boxes
    stack = [0]  # Stack to store boxes that can currently be opened

    while stack:
        box = stack.pop()

        if box not in visited:
            visited.add(box)
            keys = boxes[box]

            for key in keys:
                if key < n:
                    stack.append(key)

    return len(visited) == n
