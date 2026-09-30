import os
import unittest

from scoring import (
    calculate_percentage,
    get_performance_band,
    calculate_category_percentages
)
from validation import validate_name


class TestIQTester(unittest.TestCase):

    def test_percentage_calculation(self):
        self.assertEqual(calculate_percentage(8, 10), 80.0)

    def test_zero_total(self):
        self.assertEqual(calculate_percentage(5, 0), 0.0)

    def test_performance_band(self):
        self.assertEqual(get_performance_band(95), "Excellent")
        self.assertEqual(get_performance_band(80), "Strong")
        self.assertEqual(get_performance_band(65), "Good")
        self.assertEqual(get_performance_band(45), "Average")
        self.assertEqual(get_performance_band(20), "Needs Improvement")

    def test_category_percentages(self):
        data = {
            "Logic": {"correct": 3, "total": 4},
            "Pattern": {"correct": 2, "total": 2}
        }

        result = calculate_category_percentages(data)

        self.assertEqual(result["Logic"], 75.0)
        self.assertEqual(result["Pattern"], 100.0)

    def test_valid_name(self):
        valid, result = validate_name("Rahul Sharma")

        self.assertTrue(valid)
        self.assertEqual(result, "Rahul Sharma")

    def test_empty_name(self):
        valid, result = validate_name("")

        self.assertFalse(valid)

    def test_invalid_name(self):
        valid, result = validate_name("Rahul123")

        self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main()