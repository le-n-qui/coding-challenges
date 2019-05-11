# Experiment with walk() from module os
# Qui Le
# May 6, 2019

# Objective: Create a script to display information
# within a directory given by a developer. This script
# will systematically and recursively look inside
# each subdirectory if there is any.

# Below Is What We Can Expect to See
# Name of Directory
# List of Subdirectories
# List of Files


# Import os.walk()
from os import walk

# Example of a directory path for testing
dir_path = '/Users/lnq/Downloads/Ex_Files_SQL_EssT/Exercise Files' 

# What does function organize_directory do?
# Input: an absolute path on the user system
# Output: a dictionary that maps (sub)directory's name
#        to a dictionary that contains list of 
#        subdirectories and a list of files
def organize_directory(abs_path):
	# the dictionary to be returned 
	directory_dict = {}
	# Below we walk through the directory at abs_path 
	# using walk() from module os
	for directory_name, subdir_list, files_list in walk(abs_path):
		# Here, we have access to the name of directory
		# as well as the list of subdirectories and list of files

		# we map directory_name to an empty dictionary first
		directory_dict[directory_name] = {}
		# then we access this nested dictionary to map 
		# 'subdirectories' to subdir_list
		directory_dict[directory_name]['subdirectories'] = subdir_list
		# we map 'files' to files_list
		directory_dict[directory_name]['files'] = files_list

	return directory_dict

# We will organize contents of the given directory
# in a different format with below function
# Directory and subdirectory will be represented by {} (dictionary).
# Essentially, we will have nested dictionary

# Below is an example of what it looks like:
# {'pathname': '/home/user/folder', 
#  'subdirectory': {'minifolder': {'pathname': '/home/user/folder/minifolder', 
#                                  'subdirectory': {} ,
#                                  'files': [] } }, 
#  'files': [] }

def construct_directory(abs_path):
	pass

def __make_directory(path, directory):	
	pass



# TEST FUNCTIONS IN THIS SCRIPT
if __name__ == '__main__':
	whole_directory = organize_directory(dir_path)
	print(whole_directory)

