import unittest
import utility


class TestUtility(unittest.TestCase):
    def test_sum(self):
        param1 = 20
        param2 = 50
        result = utility.add(param1, param2)
        self.assertEqual(result, 70)

    def test_minus(self):
        """
        A unittest test to check if our minus function works well.
        :return: (str) Ok or Failed
        """
        param1 = 20
        param2 = 50
        result = utility.minus(param1, param2)
        self.assertEqual(result, -30)

    def test_minus2(self):
        param1 = '20'
        param2 = 50
        result = utility.minus(param1, param2)
        self.assertIsInstance(result, TypeError)


class TestGame(unittest.TestCase):
    def test_game(self):
        pass


if __name__ == '__main__':
    unittest.main()
