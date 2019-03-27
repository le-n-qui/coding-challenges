# Pattern Printing
# Input: n (integer)
# Output: pattern
# If n = 3, we have 
#1*2*3*10*11*12
#--4*5*8*9
#----6*7

# Qui Le
# 03/26/2019

def pattern_printing(n):
 	# biggest number in the pattern
 	biggest_num = n * (n+1)

 	# generate all numbers in the pattern
 	# and hold them in the list
 	num_list = list(range(1, biggest_num)) 

 	
