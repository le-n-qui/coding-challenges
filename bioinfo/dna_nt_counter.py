# Bioinformatics Challenge Question
# Programmer: Andy Qui

import sys

"""
Rosalind: Problem 1

DNA string is a string constructed from the alphabet {A, C, G, T}

Given: A DNA string s of length at most 1000 nt (nucleotides).
Return: Four integers (separated by spaces) counting the 
   respective number of times that the symbols 'A', 'C', 
   'G', and 'T' occur in s.

In comments and code, you may see two terms that are used 
interchangeably and they are symbol and nucleotide.

Development Plan:
 - Create a function to count nucleotides in a sample DNA string
 - Display count results for each symbol in our function
 - Read files containing DNA strings on command line
"""



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

# Create main() function 
def main():
  pass  


# Verify tests by running this file on terminal
if __name__ == '__main__':
  main()