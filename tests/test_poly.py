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

    @parameterized.expand([
        (0, 1),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 5),
        (5, 12),
        (6, 35),
        (7, 108),
        (8, 369),
        (9, 1285),
        (10, 4655),
    ])
    def test_enumerate_poly(self, n, expected):
        poly = Poly()
        self.assertEqual(expected, len(poly.enumerate_poly(n)))

    def test_enumerate_poly_individual(self):
        poly = Poly()
        print("Length is:", len(poly.enumerate_poly(17)))

    def test_transformation_v2(self):
        poly = Poly()
        print(poly.transformations_v2([6, 5, 3]))

    bin_length_v2_test_data= [(x, 1) for x in range(1, 2)] + [(x, 2) for x in range(2, 4)] + [(x, 3) for x in range(4, 8)] + [(x, 4) for x in range(8, 16)] + [(x, 5) for x in range(16, 32)];
    @parameterized.expand(bin_length_v2_test_data)
    def test_bin_length_v2(self, n, expected):
        poly = Poly()
        self.assertEqual(expected, poly.bin_length_v2(n), n)



if __name__ == '__main__':
    unittest.main()
