#!/usr/bin/python3
"""
checks if all boxes can be opened with keys contained
in the other boxes
"""


def canUnlockAll(boxes):
    """
    argument:
    boxes - a list of lists
    returns: true if all boxes can be opened
    using indexes as keys
    """
    secondbox = []
    secondbox.append(boxes[0])
    for list in boxes:
        for i in list:
            if i < len(boxes) and list != boxes[i]:
                if boxes[i] not in secondbox:
                    secondbox.append(boxes[i])
    return len(secondbox) == len(boxes)
