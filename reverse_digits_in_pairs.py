# Coding Question
# Qui Le

import unittest

# Problem Statement: Given an integer, reverse the digits of the integer in pairs.

def reverse_digits_in_pairs(number):
	pass


# Unit Testing
class TestReverseFn(unittest.TestCase):
	def test_number_of_even_length(self):
		n = 123456
		self.assertEqual(reverse_digits_in_pairs(n), 214365)

	def test_number_of_odd_length(self):
		n = 67895
		self.assertEqual(reverse_digits_in_pairs(n), 76985)


if __name__ == '__main__':
	unittest.main()