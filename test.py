import unittest
class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        calculator = StringCalculator()
        result = calculator.add("")
        self.assertEqual(result, 0)

    def test_single_number(self):
        calculator = StringCalculator()
        result = calculator.add("1")
        self.assertEqual(result, 1)
if __name__ == '__main__':
    unittest.main()
