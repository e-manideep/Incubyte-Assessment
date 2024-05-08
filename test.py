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

if __name__ == '__main__':
    unittest.main()
