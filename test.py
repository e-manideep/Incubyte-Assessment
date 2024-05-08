import unittest
import re
class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        strnumbers = str(numbers)
        strnumbers = strnumbers.replace("\n", ",")
        numbers = strnumbers
        # if numbers.startswith("//"):
        #     delimeter, numbers = numbers.split("\n", 1)
        #     delimeter = delimeter[2:]
        # numbers_list = re.split(r'[,\\' + delimeter + ']', numbers)
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
    
    def test_newline_seperator(self):
        calculator = StringCalculator()
        result = calculator.add("1\n2,3")
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
