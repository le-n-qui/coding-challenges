# Rosalind: Problem 1
# DNA string is a string constructed from the alphabet {A, C, G, T}
# Given: A DNA string s of length at most 1000 nt (nucleotides).
# Return: Four integers (separated by spaces) counting the 
#   respective number of times that the symbols 'A', 'C', 
#   'G', and 'T' occur in s.

import unittest

# Define function to count
# nucleotides in a DNA string
def dna_nt_counter(sample):
	# create a counter dictionary to 
	# keep count of each symbol
	counter = dict()
	for symbol in sample:
		# if this is the first time 
		# seeing the current symbol
		if counter.get(symbol, -1) == -1:  
			counter[symbol] = 1 # record 1
		else:
			# otherwise increment symbol's count by 1
			counter[symbol] += 1
	print(f"{counter['A']} {counter['C']} {counter['G']} {counter['T']}")

# Make a Unit Test class
class TestStringDNA(unittest.TestCase):
	pass

# Verify tests by running this file on terminal
if __name__ == '__main__':
 	unittest.main(verbosity=3) 