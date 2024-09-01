import unittest
from freepoly.poly import Poly
import pytest
from parameterized import parameterized

class MyTestCase(unittest.TestCase):

    @parameterized.expand([
        (2, 1, [2,3,2], [2,3,3]),
        (0, 0, [1,1,1], [3,2,2]),
    ])
    def test_poly_right(self, r, c, free_poly, expected):
        poly = Poly()
        self.assertEqual(expected, poly.poly_right(r, c, free_poly))  # add assertion here

    @parameterized.expand([
        (0, 0, [3, 2], [3, 3])
    ])
    def test_poly_bottom(self, r, c, free_poly, expected):
        poly = Poly()
        self.assertEqual(expected, poly.poly_bottom(r, c, free_poly))  # add

    @parameterized.expand([
        (1, 1, [1, 3], [3, 3])
    ])
    def test_poly_top(self, r, c, free_poly, expected):
        poly = Poly()
        self.assertEqual(expected, poly.poly_top(r, c, free_poly))  #

    def test_enumerate_poly(self):
        poly = Poly()
        p = poly.enumerate_poly(13)
        print(len(p))
        # print(p)

if __name__ == '__main__':
    unittest.main()
