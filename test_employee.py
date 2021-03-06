import unittest
from unittest.mock import patch
from shop.employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Let's say we need to populate our database here!")

    @classmethod
    def tearDownClass(cls) -> None:
        print("We depopulate our database here!")

    def setUp(self) -> None:
        self.emp1 = Employee('Michael', 'Jamie', 450000)
        self.emp2 = Employee('Mark', 'Eke', 900000)

    def test_email(self):
        self.assertEqual(self.emp1.email, "michael.jamie@decagon.dev")
        self.assertEqual(self.emp2.email, "mark.eke@decagon.dev")

        self.emp1.first_name = "jerry"
        self.emp2.last_name = "flieer"

        self.assertEqual(self.emp1.email, "jerry.jamie@decagon.dev")
        self.assertEqual(self.emp2.email, "mark.flieer@decagon.dev")

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, "Michael Jamie")
        self.assertEqual(self.emp2.fullname, "Mark Eke")

        self.emp1.first_name = "dani"
        self.emp2.last_name = "fuller"

        self.assertEqual(self.emp1.fullname, "Dani Jamie")
        self.assertEqual(self.emp2.fullname, "Mark Fuller")

    def test_apply_raise(self):
        self.emp2.apply_raise()
        self.emp1.apply_raise()

        self.assertEqual(self.emp1.pay, 472500)
        self.assertEqual(self.emp2.pay, 945000.00)

    def test_schedule(self):
        with patch('shop.employee.request') as mocked:
            mocked.return_value.ok = True
            mocked.return_value.text = 'Success'
            schedule = self.emp1.get_schedule()
            print(schedule)
            mocked.assert_called_with('GET', 'https://company.com')
            self.assertEqual(schedule, 'Success')

            mocked.return_value.ok = False
            schedule = self.emp2.get_schedule('https://platform.com')
            print(schedule)
            mocked.assert_called_with('GET', 'https://platform.com')
            self.assertEqual(schedule, 'Bad response')


if __name__ == '__main__':
    unittest.main()
