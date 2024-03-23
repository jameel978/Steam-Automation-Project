import unittest

class MathTestCase(unittest.TestCase):
    def test_addition(self):
        test_cases = [
            (1, 2, 3),    # Test case: 1 + 2 = 3
            (5, 5, 10),   # Test case: 5 + 5 = 10
            (0, 0, 0),    # Test case: 0 + 0 = 0
            (-1, 1, 0),   # Test case: -1 + 1 = 0
            (10, -5, 5)   # Test case: 10 + (-5) = 5
        ]
        for a, b, expected_sum in test_cases:
            with self.subTest(a=a, b=b):
                result = self.add(a, b)
                self.assertEqual(result, expected_sum)

    def add(self, a, b):
        return a + b

if __name__ == "__main__":
    unittest.main()
