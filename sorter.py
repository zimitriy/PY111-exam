import random
import time
from typing import List
import operator


def sort(container) -> list:
    if len(container) > 1:

        mid = len(container) // 2

        left = container[:mid]

        right = container[mid:]

        sort(left)

        sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                container[k] = left[i]
                i += 1
            else:
                container[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            container[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            container[k] = right[j]
            j += 1
            k += 1

    return container

