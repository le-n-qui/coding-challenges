# Coding Question
# Qui Le

import unittest

# Problem Statement: Given an integer, reverse the digits of the integer in pairs.

# This function will use Python list as a stack
# data structure to store digits of integer
def reverse_digits_in_pairs(number):
	# Need a stack
	stack = []
	# Need a result variable
	result = 0
	# With a while loop, get each digit of integer starting at the last one
	while number:
		# Keep digits in stack
		stack.append(number % 10) # modulo 10 gives last digit
		number //= 10 # Get the integer without last digit
	# While stack is not empty, do two pop operations 
	while stack:
		first_digit = stack.pop()
		# Need a test condition for the second pop because stack may have only one item left
		if stack:
			second_digit = stack.pop()
			# Create reversed pairs of of digits and add it to result
			result = (result * 100) + (second_digit * 10) + first_digit
		else:
			# because second digit does not exist
			# multiply result by 10 and add first digit
			result = (result * 10) + first_digit
		
	# Return result
	return result

# Unit Testing
class TestReverseFn(unittest.TestCase):
	def test_number_of_even_length(self):
		n = 123456
		self.assertEqual(reverse_digits_in_pairs(n), 214365)

	def test_number_of_odd_length(self):
		n = 67895
		self.assertEqual(reverse_digits_in_pairs(n), 76985)

	def test_number_with_one_zero_digit(self):
		n1 = 120445
		n2 = 124045
		self.assertEqual(reverse_digits_in_pairs(n1), 214054)
		self.assertEqual(reverse_digits_in_pairs(n2), 210454)

	def test_number_with_last_two_zero_digits(self):
		n = 568900
		self.assertEqual(reverse_digits_in_pairs(n), 659800)

	def test_number_zero_digit_at_second_from_left(self):
		n = 603211
		self.assertEqual(reverse_digits_in_pairs(n), 62311)

if __name__ == '__main__':
	unittest.main(verbosity=3)