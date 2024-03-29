# Bioinformatics Challenge Question
# Programmer: Andy Qui

import sys

"""
DNA string is a string constructed from the alphabet {A, C, G, T}

Given: A DNA string s of length at most 1000 nt (nucleotides).
Return: Four integers (separated by spaces) counting the 
   respective number of times that the symbols 'A', 'C', 
   'G', and 'T' occur in s.

In comments and code, you may see two terms that are used 
interchangeably and they are symbol and nucleotide.

Development Plan:
 - Read files containing DNA strings on command line
 - Create a function to accept a file and read the content
 - Within the function, count nucleotides in a sample DNA string
 - Return count results for each symbol in our function
 - Print out result or write it to files
"""



# Define function to count
# nucleotides in a DNA string
def dna_nt_counter(filename):
  # create a counter dictionary to 
  # keep count of each symbol
  counter = dict()

  # Open file to read content 
  with open(filename, 'r') as f:
    # Be careful about using read() 
    # in case where file size is too big 
    sample = f.read() 
    # Iterate through sample string, one symbol at a time
    for symbol in sample:
      # if this is the first time 
      # seeing the current symbol
      if counter.get(symbol, -1) == -1:  
        counter[symbol] = 1 # record 1
      else:
        # otherwise increment symbol's count by 1
        counter[symbol] += 1

  return f"{counter['A']} {counter['C']} {counter['G']} {counter['T']}"

# Create main() function 
def main():
  # Make a list of command line arguments omitting
  # the [0] element which is the script itself
  args = sys.argv[1:]

  # no args present
  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it
  # from args if it is present
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # Process files in args list
  # For each file, get a one-liner result
  # either print the text
  # or write it to a summary file
  for file in args:
    result = dna_nt_counter(file)
    if summary == False:
      print(result)
    else:
      summary_file = file + '.summary'
      with open(summary_file, 'w') as f:
        f.write(result) 


# Verify tests by running this file on terminal
if __name__ == '__main__':
  main()