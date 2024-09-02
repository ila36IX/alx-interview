#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """Check if all the boxes can be unlocked"""
    if len(boxes) == 0:
        return True
    check = [False for _ in boxes]
    next_boxes = set([0])
    seen_boxes = set([])
    while len(next_boxes):
        next_boxes_buff = set([])
        for box_key in next_boxes:
            for key in boxes[box_key]:
                if key not in seen_boxes and key < len(boxes):
                    check[key] = True
                    next_boxes_buff.add(key)
            check[box_key] = True
            seen_boxes.add(box_key)
            next_boxes = next_boxes_buff
    return all(check)
