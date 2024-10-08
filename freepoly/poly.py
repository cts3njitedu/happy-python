from collections import deque
from math import log2, floor

class Poly:

    def bin_length(self, n):
        return len(bin(n)[2:])

    def bin_length_v2(self, n):
        return floor(log2(n)/log2(2)) + 1

    def enumerate_poly(self, n):
        if n == 0:
            return [[]]
        if n == 1:
            return [[n]]
        free_poly_queue = deque()
        root = [1]
        free_poly_queue.append(root)
        free_poly_set = {str(root)}
        for i in range(2, n + 1):
            size = len(free_poly_queue)
            while size > 0:
                poly = free_poly_queue.popleft()
                for r, rv in enumerate(poly):
                    column_size = self.bin_length_v2(rv)
                    for c in range(column_size):
                        if rv & 1 << c != 0:
                            self.save_poly(free_poly_set, free_poly_queue, self.poly_top(r, c, poly))
                            self.save_poly(free_poly_set, free_poly_queue, self.poly_right(r, c, poly))
                            self.save_poly(free_poly_set, free_poly_queue, self.poly_bottom(r, c, poly))
                            self.save_poly(free_poly_set, free_poly_queue, self.poly_left(r, c, poly))
                size = size - 1
            free_poly_set.clear()
        return free_poly_queue

    def save_poly(self, free_poly_set, free_poly_queue, poly_n):
        if poly_n is not None:
            isUniquePoly = self.is_unique_poly(free_poly_set, poly_n)
            if isUniquePoly:
                free_poly_set.add(str(poly_n))
                free_poly_queue.append(poly_n)

    def poly_top(self, r, c, poly):
        top = r == 0 or (poly[r - 1] & 1 << c == 0)
        if top:
            poly_copy = poly.copy()
            if r == 0:
                return [1<<c] + poly_copy
            poly_copy[r - 1] |= 1<<c
            return poly_copy

    def poly_right(self, r, c, poly):
        right = c == 0 or (poly[r] & 1 << (c - 1) == 0)
        if right:
            if c == 0:
                fn = lambda row : row << 1
                poly_copy = list(map(fn, poly))
                poly_copy[r] |= 1
                return poly_copy
            else:
                poly_copy = poly.copy()
                poly_copy[r] |= 1<<(c-1)
                return poly_copy

    def poly_bottom(self, r, c, poly):
        bottom = r == len(poly) - 1 or (poly[r + 1] & 1 << c == 0)
        if bottom:
            poly_copy = poly.copy()
            if r == len(poly_copy) - 1:
                return poly_copy + [1<<c]
            poly_copy[r + 1] |= 1<<c
            return poly_copy

    def poly_left(self, r, c, poly):
        left = poly[r] & 1 << (c + 1) == 0
        if left:
            poly_copy = poly.copy()
            poly_copy[r] |= 1 << (c + 1)
            return poly_copy

    def is_unique_poly(self, free_poly_set, free_poly):
        if str(free_poly) in free_poly_set:
            return False
        transformations = self.transformations(free_poly)
        for t in transformations:
            free_poly_set.add(str(t))
        return True

    def transformations(self, poly):
        cs = max([self.bin_length_v2(x) for x in poly])
        rs = len(poly)
        top_right_left = [0] * rs
        top_left_right = [0] * rs
        right_top_bottom = [0] * cs
        right_bottom_top = [0] * cs
        bottom_left_right = [0] * rs
        bottom_right_left = [0] * rs
        left_top_bottom = [0] * cs
        left_bottom_top = [0] * cs
        for r, rv in enumerate(poly):
            for c in range(0, cs):
                v = 0 if rv & (1 << c) == 0 else 1
                top_right_left[r] |= (v << c)
                top_left_right[r] |= (v << (cs - c - 1))
                bottom_right_left[rs - r - 1] |= (v << c)
                bottom_left_right[rs-r-1] |= (v << (cs - c - 1))
                right_top_bottom[c] |= (v << r)
                right_bottom_top[c] |= (v << (rs - r - 1))
                left_top_bottom[cs - c - 1] |= (v << r)
                left_bottom_top[cs - c - 1] |= (v << (rs - r - 1))
        return [top_right_left, top_left_right, right_top_bottom, right_bottom_top, bottom_right_left,
         bottom_left_right, left_top_bottom, left_bottom_top]