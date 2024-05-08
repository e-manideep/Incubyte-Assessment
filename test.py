import unittest
import re
class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        strnumbers = str(numbers)
        strnumbers = strnumbers.replace("\n", ",")
        numbers = strnumbers

        delimiter = ","
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[4:]
            strnumbers = str(numbers)
            strnumbers = strnumbers.replace("\n", delimiter)
            numbers = strnumbers

        total = 0
        negatives = []

        for num in numbers.split(delimiter):
            try:
                num = int(num)
                if num < 0:
                    negatives.append(str(num))
                elif num <= 1000:
                    total += num
            except ValueError:
                pass

        if negatives:
            raise ValueError("Negative numbers not allowed: " + ", ".join(negatives))

        return total


        

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
    
    def test_newline_seperator(self):
        calculator = StringCalculator()
        result = calculator.add("1\n2,3")
        self.assertEqual(result, 6)

    def test_custom_delimiter(self):
        calculator = StringCalculator()
        result = calculator.add("//;\n1;2")
        self.assertEqual(result, 3)
    
    def test_negative_numbers(self):
        calculator = StringCalculator()
        with self.assertRaises(ValueError) as context:
            calculator.add("-1,2,-3")
        self.assertTrue("Negative numbers not allowed: -1, -3" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
