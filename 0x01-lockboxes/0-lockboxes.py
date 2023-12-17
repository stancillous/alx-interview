#!/usr/bin/python3
"""Implement canUnlockAll function"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""

    # determine the keys required to open the boxes
    keysReq = []
    for key in range(1, len(boxes)):
        keysReq.append(key)

    # print (f"***keys required: {keysReq}***")

    # open the first box and see what keys are present in the keysReq
    # create a list of keys collected
    keysCol = []

    for key in boxes[0]:
        keysCol.append(key)

    noKeys = False

    while (noKeys is False):

        keyCount = 0

        for key in keysReq.copy():
            if key in keysCol:
                # print(f"Found {key} in {keysCol}")
                for i in boxes[key]:
                    if i not in keysCol:
                        keysCol.append(i)

                keysReq.remove(key)

                # print(f"Remove box {key} from required keys: {keysReq}")

                keyCount += 1

            else:
                pass
                # print(f"Key for box {key} not found in {keysCol}")

        if keyCount > 0:
            noKeys = False

        else:
            noKeys = True

    if keysReq:
        return False

    else:
        return True
