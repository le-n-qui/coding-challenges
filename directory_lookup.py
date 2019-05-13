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
	directory = {}
	for current_dir_name, subdir_list, files_list in walk(abs_path):
		directory = __make_directory(directory, current_dir_name, subdir_list, files_list)
	return directory

def __make_directory(directory, dir_name, subdir_list, files_list):	
	
	if directory == {}: # handle the parent (first) directory (level 1)	
		directory['pathname'] = dir_name
		directory['subdirectories'] = {}
		for subdir_name in subdir_list:
			directory['subdirectories'][subdir_name] = {}
		directory['files'] = files_list
		return directory
	
	else: # if there are more than 1 level (children and grandchildren directories)

		# Split dir_name into a list of distinct names
		names_in_dir_name = dir_name.split('/') # child dir_name
		# Also, split parent directory's pathname into a list of distinct name
		names_in_parent_dir = directory['pathname'].split('/')
		
		# Currently, we are at level 1
		current_directory = directory
		# Below we move out of level 1
		# With each iteration, we move into the correct subdirectory of next level
		# NOTE: we slice names_in_dir_name list to get names of subdirectories only
		for name in names_in_dir_name[len(names_in_parent_dir):]: 
			# below we are changing our current directory 
			current_directory = current_directory['subdirectories'][name]

		# At the end of loop, we are inside the innermost subdirectory, which is empty
		# we make a recursive call to __make_directory  
		# to update current directory with new given info
		current_directory = __make_directory(current_directory, dir_name, subdir_list, files_list)

	return directory 
	


# TEST FUNCTIONS IN THIS SCRIPT
if __name__ == '__main__':
	print("***FIRST TEST***")
	whole_directory = organize_directory(dir_path)
	print(whole_directory)

	# test construct_directory
	print("\n***SECOND TEST***")
	dir_dict = construct_directory(dir_path)
	print(dir_dict)

