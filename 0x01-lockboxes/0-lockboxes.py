#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """Check if all the boxes can be unlocked"""
    check = [False for _ in boxes]
    check[0] = True
    canUnlockAll_help(boxes, check, 0)
    return all(check)


def canUnlockAll_help(boxes, check, i):
    """Check if all the boxes can be unlocked using recursion"""
    for key in boxes[i]:
        if key <= len(boxes) and check[key] is False:
            check[key] = True
            canUnlockAll_help(boxes, check, key)
