import unittest
from even_fibonacci_num import even_fibonacci_pairs

# test_fibonacci.py


class TestFibonacci(unittest.TestCase):

    def test_even_fibonacci_pairs_10(self):
        result = even_fibonacci_pairs(10)
        self.assertEqual(result, [
                         2, 8], "Fibonacci even numbers below 10 should be [2, 8]")

    def test_even_fibonacci_pairs_4000000(self):
        result = even_fibonacci_pairs(4000000)
        self.assertEqual(result, [2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578],
                         "Fibonacci even numbers below 4,000,000 should be [2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578]")


if __name__ == '__main__':
    unittest.main()
