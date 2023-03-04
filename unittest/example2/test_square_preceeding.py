"""
Test module for square_preceding.py
"""
import unittest
from square_preceding import square_preceding

class TestSquarePreceding(unittest.TestCase):
    def test_square_preceding(self):
        L = [1, 2, 3]
        square_preceding(L)
        self.assertEqual(L, [0, 1, 4])

        L = [5, 10, -5]
        square_preceding(L)
        self.assertEqual(L, [0, 25, 100])

        L = [2]
        square_preceding(L)
        self.assertEqual(L, [0])

        L = []
        square_preceding(L)
        self.assertEqual(L, [])

if __name__ == '__main__':
    unittest.main()

