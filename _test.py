import unittest
import utility

class TestUtility(unittest.TestCase):
    def test_sum(self):
        param1 = 20
        param2 = 50
        result = utility.add(param1, param2)
        self