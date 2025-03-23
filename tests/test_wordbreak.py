import unittest

from wordbreak.wordbreak import WordBreak


class MyTestCase(unittest.TestCase):
    def test_getCombinations(self):
        wb = WordBreak()
        print(wb.get_combinations("wordbreakproblem",
                                  ["this", "th", "is", "famous", "word", "break",
                                   "b", "r", "e", "a", "k", "br", "bre",
                                   "brea", "ak", "problem"]))
