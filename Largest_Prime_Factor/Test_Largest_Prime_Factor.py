import unittest
from Largest_Prime_Factor import largest_prime_factor

# test_prime_factor.py


class TestPrimeFactor(unittest.TestCase):

    def test_largest_prime_factor_13195(self):
        result = largest_prime_factor(13195)
        self.assertEqual(
            result, 29, "El factor primo más grande de 13195 debería ser 29")

    def test_largest_prime_factor_600851475143(self):
        result = largest_prime_factor(600851475143)
        self.assertEqual(
            result, 6857, "El factor primo más grande de 600851475143 debería ser 6857")


if __name__ == '__main__':
    unittest.main()
