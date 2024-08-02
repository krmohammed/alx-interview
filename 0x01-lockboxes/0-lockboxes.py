#!/usr/bin/python3
"""Provides the fuction canUnlockAll"""


def canUnlockAll(boxes):
    """unlocks all boxes in the boxes array
    Args:
        boxes (list): A list of lists
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key in range(len(boxes)) and not unlocked[key]:
            unlocked[key] = True
            keys.update(boxes[key])
    return all(unlocked)
