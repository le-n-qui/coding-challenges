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

 	# Printing left half of the pattern
 	# stopping at the multiply sign in the middle
 	# Left half contains n left groups of decreasing size
 	# Similar to right haft
 	# However, pay attention to dashes for left half

 	# begin of left group
 	start_of_left = 0
 	# end of left group
 	end_of_left = 0

 	# begin of right group
 	start_of_right = biggest_num
 	# end of right group
 	end_of_right = 0 

 	# size of groups decrease with each iteration
 	for size in range(n, 0, -1):
 		# assign start point and endpoint for each group
 		# in first iteration: start_of_left is 0 and end_of_left is n
 		# later iterations, this updates end_of_left
 		end_of_left = end_of_left + size

 		# Update start_of_right
 		start_of_right = start_of_right - size
 		
 		
 		# Write code below to print left half of pattern
 		
 		# Update end_of_right
 		end_of_right = start_of_right + size

 		
 		# Write code below to print right half of pattern

 		# Update start_of_left
 		start_of_left = start_of_left + size


