import json
import unittest

from sternbrocot.stern_brocot import SternBrocot


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sternBrocot = SternBrocot()
        tree = sternBrocot.getSternBrocotTree(4)
        print(json.dumps(tree.to_dict(), indent=4))


if __name__ == '__main__':
    unittest.main()
