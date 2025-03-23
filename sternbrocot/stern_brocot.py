import queue


class SternBrocotTree:
    def __init__(self, left_fraction, fraction, right_fraction, level):
        self.left_fraction = left_fraction
        self.fraction = fraction
        self.right_fraction = right_fraction
        self.left_child = None
        self.right_child = None
        self.level = level

    def to_dict(self):
        left_child_dict = None
        right_child_dict = None
        dict = {
            "fraction": f"{self.fraction[0]}{'/'}{self.fraction[1]}"
        }
        if self.left_child:
            dict["left"] = self.left_child.to_dict()

        if self.right_child:
            dict["right"] = self.right_child.to_dict()

        return dict


class SternBrocot:
    def getSternBrocotTree(self, level):
        t = SternBrocotTree((0, 1), (1, 1), (1, 0), 1)
        q = queue.Queue()
        q.put(t)
        while not q.empty():
            size = q.qsize()
            while size > 0:
                tt = q.get()
                if tt.level < level:
                    tt.left_child = SternBrocotTree(tt.left_fraction,
                                                    self.add_fractions(tt.left_fraction, tt.fraction),
                                                    tt.fraction, tt.level + 1)
                    q.put(tt.left_child)
                    tt.right_child = SternBrocotTree(tt.fraction,
                                                     self.add_fractions(tt.fraction, tt.right_fraction),
                                                     tt.right_fraction, tt.level + 1)
                    q.put(tt.right_child)
                    tt.left_fraction = ()
                    tt.right_fraction = ()
                size = size - 1
        return t

    @staticmethod
    def add_fractions(f1, f2):
        return f1[0] + f2[0], f1[1] + f2[1]
