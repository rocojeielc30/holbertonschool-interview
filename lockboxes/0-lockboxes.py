#!/usr/bin/python3
"""Defines a function that solves the lockboxes problem."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else False."""
    opened = {0}  # box 0 starts unlocked
    keys_to_try = list(boxes[0])  # copy so we don't modify the input

    while len(keys_to_try) > 0:  # keep going while we still have keys
        key = keys_to_try.pop()  # take one key off the pile
        if key >= len(boxes) or key in opened:  # no such box, or already open
            continue
        opened.add(key)  # open the box and add it to set 
        keys_to_try.extend(boxes[key])  # collect keys inside the box

    return len(opened) == len(boxes)  # compare num of boxes opened to boxes given
