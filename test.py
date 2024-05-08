import unittest
class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        return sum(int(num) for num in numbers.split(","))

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        calculator = StringCalculator()
        result = calculator.add("")
        self.assertEqual(result, 0)

    def test_single_number(self):
        calculator = StringCalculator()
        result = calculator.add("1")
        self.assertEqual(result, 1)
    
    def test_multiple_numbers(self):
        calculator = StringCalculator()
        result = calculator.add("1,2")
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
