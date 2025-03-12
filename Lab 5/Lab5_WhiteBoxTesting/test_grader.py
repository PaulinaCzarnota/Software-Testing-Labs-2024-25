import unittest
import math
from grader import get_grade_classification

class TestGrader(unittest.TestCase):
    """
    Unit tests for the get_grade_classification function.
    """

    def test_fail_case(self):
        """Test failing cases (0-39)."""
        self.assertEqual(get_grade_classification(20), "Fail")
        self.assertEqual(get_grade_classification(39), "Fail")
        self.assertEqual(get_grade_classification(0), "Fail")

    def test_pass_case(self):
        """Test pass cases (40-49)."""
        self.assertEqual(get_grade_classification(40), "Pass")
        self.assertEqual(get_grade_classification(49), "Pass")

    def test_2ii_case(self):
        """Test cases for '2.ii' classification (50-59)."""
        self.assertEqual(get_grade_classification(50), "2.ii")
        self.assertEqual(get_grade_classification(55), "2.ii")
        self.assertEqual(get_grade_classification(59), "2.ii")

    def test_2i_case(self):
        """Test cases for '2.i' classification (60-69)."""
        self.assertEqual(get_grade_classification(60), "2.i")
        self.assertEqual(get_grade_classification(65), "2.i")
        self.assertEqual(get_grade_classification(69), "2.i")

    def test_1_case(self):
        """Test cases for '1' classification (70-100)."""
        self.assertEqual(get_grade_classification(70), "1")
        self.assertEqual(get_grade_classification(85), "1")
        self.assertEqual(get_grade_classification(100), "1")

    def test_boundary_cases(self):
        """Ensure correct classification for edge boundary values."""
        self.assertEqual(get_grade_classification(39.9), "Fail")
        self.assertEqual(get_grade_classification(40.0), "Pass")
        self.assertEqual(get_grade_classification(49.9), "Pass")
        self.assertEqual(get_grade_classification(50.0), "2.ii")
        self.assertEqual(get_grade_classification(59.9), "2.ii")
        self.assertEqual(get_grade_classification(60.0), "2.i")
        self.assertEqual(get_grade_classification(69.9), "2.i")
        self.assertEqual(get_grade_classification(70.0), "1")

    def test_invalid_inputs(self):
        """Test cases for invalid inputs."""
        invalid_values = [
            "abc", None, [], {}, 150, -5,  # Non-number values
            float('inf'), float('-inf'), math.nan,  # Infinite and NaN
            True, False,  # Boolean values
            set(), tuple(), "", b"50", b"100"  # Byte strings and empty data types
        ]

        for value in invalid_values:
            with self.assertRaises(ValueError, msg=f"Failed for input: {value}"):
                get_grade_classification(value)

    def test_integer_vs_float(self):
        """Ensure integers and floats are handled correctly."""
        self.assertEqual(get_grade_classification(40), "Pass")
        self.assertEqual(get_grade_classification(60.5), "2.i")
        self.assertEqual(get_grade_classification(70.9), "1")

    def test_exact_40(self):
        """Test case for exactly 40.0."""
        self.assertEqual(get_grade_classification(40.0), "Pass")

if __name__ == "__main__":
    unittest.main()  # pragma: no cover