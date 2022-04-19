"""Test case for Employee class."""

from e11_3_employee_class_testing import Employee
import unittest


class TestCaseEmployee(unittest.TestCase):
    """Series of tests for the Employee Class"""

    def setUp(self):
        """Create an Employee for use on all of our test methods."""
        self.my_employee = Employee('John', 'Doe', 27_500)

    def test_give_default_raise(self):
        """Check if salary increases by $5,000 by default."""
        previous_salary = self.my_employee.annual_salary
        self.my_employee.give_raise()
        self.assertEqual(
            self.my_employee.annual_salary, previous_salary + 5000)

    def test_give_custom_raise(self):
        """Check if salary is increased by the amount provided."""
        previous_salary = self.my_employee.annual_salary
        increase = 10_000
        self.my_employee.give_raise(increase)
        self.assertEqual(self.my_employee.annual_salary,
                         previous_salary + increase)


if __name__ == '__main__':
    unittest.main()
