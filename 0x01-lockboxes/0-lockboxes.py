#!/usr/bin/python3
"""Lockboxes Mock Interview"""

from collections import deque


def canUnlockAll(boxes):
    # Get the number of boxes
    n = len(boxes)
    # Created a list indicating if all boxes were visited
    # and dill all the n boxes with false since none has been unlocked
    visited = [False] * n

    # Change the first box to true since it is unlocked
    visited[0] = True

    # Put the first box to the qeque for exploration of keys
    # since it has been unlocked
    queue = deque([0])

    # Iterate all the boxes in the deque untill there is none
    # using a while loop
    while queue:
        # Get the leftmost box, (simply, the one starting)
        current_box = queue.popleft()
        # Iterate through all the keys in the box
        for key in boxes[current_box]:
            # Check if any of them has not been used to unlock a box
            if key < n and not visited[key]:
                # Once we get the key we set the box to true, meaning
                # it has been unlocked
                visited[key] = True
                # Then append the box to queue for exploration
                queue.append(key)

    # Check if all have been visited to return True or Flase if not
    return all(visited)
