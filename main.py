import unittest
import random

import sorter as sorter


class MyTestCase(unittest.TestCase):
    def test_sorted(self):
        arr = [random.randint(-100, 100) for _ in range(30)]
        a = len(arr) - 1
        out = list()
        while a > 0:
            out.append(arr[a])
            a = int(a // 1.7)
        self.assertEqual(
            sorted(arr),
            sorter.sort(arr)
        )


if __name__ == '__main__':
    unittest.main()
