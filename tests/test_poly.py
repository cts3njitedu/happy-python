import unittest
from unittest import skipIf

from freepoly.poly import Poly
import numpy as np
from parameterized import parameterized

class MyTestCase(unittest.TestCase):

    @parameterized.expand([
        (2, 1, [2,3,2], [2,3,3]),
        (0, 0, [1,1,1], [3,2,2]),
        (1, 2, [7,4,7], [7,6,7]),
        (0, 0, [1], [3])
    ])
    def test_poly_right(self, r, c, free_poly, expected):
        poly = Poly()
        np.testing.assert_array_equal(expected, poly.poly_right(r, c, free_poly))

    @parameterized.expand([
        (0, 0, [3, 2], [3, 3]),
        (2, 2, [11, 11, 15], [11, 11, 15, 4]),
    ])
    def test_poly_bottom(self, r, c, free_poly, expected):
        poly = Poly()
        np.testing.assert_array_equal(expected, poly.poly_bottom(r, c, free_poly))

    @parameterized.expand([
        (0, 2, [4, 7, 1], [12, 7, 1]),
        (1, 2, [4, 7, 1], [4, 15, 1]),
        (2, 0, [4, 7, 1], [4, 7, 3]),
    ])
    def test_poly_left(self, r, c, free_poly, expected):
        poly = Poly()
        np.testing.assert_array_equal(expected, poly.poly_left(r, c, free_poly))

    @parameterized.expand([
        (1, 1, [1, 3], [3, 3]),
        (0, 0, [1,1,1], [1,1,1,1]),
        (1, 2, [1, 7, 7], [5, 7, 7]),
        (1, 1, [1, 7, 7], [3, 7, 7])
    ])
    def test_poly_top(self, r, c, free_poly, expected):
        poly = Poly()
        np.testing.assert_array_equal(np.array(expected, dtype=np.uint64), poly.poly_top(r, c, free_poly))  #

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
        print("Length is:", len(poly.enumerate_poly(10)))

    def test_transformation_v2(self):
        poly = Poly()
        print(poly.transformations_v2([13, 15, 3]))

    bin_length_v2_test_data= [(x, 1) for x in range(1, 2)] + [(x, 2) for x in range(2, 4)] + [(x, 3) for x in range(4, 8)] + [(x, 4) for x in range(8, 16)] + [(x, 5) for x in range(16, 32)];
    @parameterized.expand(bin_length_v2_test_data)
    def test_bin_length_v2(self, n, expected):
        poly = Poly()
        self.assertEqual(expected, poly.bin_length_v2(n), n)



if __name__ == '__main__':
    unittest.main()
