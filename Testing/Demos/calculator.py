import unittest

class Calculator:

    @staticmethod
    def sum_nums(nums):
        return sum(num for num in nums)

    @staticmethod
    def multiply_nums(nums):
        product = 1
        for num in nums:
            product *= num
        return product

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.nums = (1, 2, 3, 4)

    def test_sum_func__when_valid_nums__expect_correct_result(self):
        self.assertEqual(Calculator().sum_nums(self.nums), 10)

    def test_multiply_func__when_valid_nums__expect_correct_result(self):
        self.assertEqual(Calculator().multiply_nums(self.nums), 24)

if __name__ == "__main__":
    unittest.main()