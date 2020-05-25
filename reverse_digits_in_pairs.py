# Coding Question
# Qui Le

import unittest

# Problem Statement: Given an integer, reverse the digits of the integer in pairs.

# This function will use Python list as a stack
# data structure to store digits of integer
def reverse_digits_in_pairs(number):
	# Need a stack
	# Need a result variable
	# With a while loop, get each digit of integer starting at the last one
	# Keep digits in stack
	# While stack is not empty, do two pop operations 
	# Need a test condition for the second pop because stack may have only one item left
	# Create reversed pairs of of digits and add it to result
	# Return result
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