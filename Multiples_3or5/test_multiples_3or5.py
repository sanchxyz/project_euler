import unittest
from multiples_3or5 import sum_of_multiples


class TestMultiples3or5(unittest.TestCase):

    def test_sum_of_multiples_3_5_below_10(self):
        result = sum_of_multiples(3, 5, 10)
        self.assertEqual(
            result, 23, "La suma de los múltiplos de 3 y 5 por debajo de 10 debería ser 23")

    def test_sum_of_multiples_3_5_below_1000(self):
        result = sum_of_multiples(3, 5, 1000)
        self.assertEqual(
            result, 233168, "La suma de los múltiplos de 3 y 5 por debajo de 1000 debería ser 233168")

    def test_sum_of_multiples_3_3_below_3(self):
        result = sum_of_multiples(3, 3, 3)
        self.assertEqual(
            result, 0, "La suma de los múltiplos de 3 y 3 por debajo de 3 debería ser 0")


if __name__ == '__main__':
    unittest.main()
