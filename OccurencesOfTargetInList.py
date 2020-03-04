# Google Coding Interview Problem: 
# Given a sorted array of integers, find the number of occurences of a given target value.

#  Input:  [5,7,7,8,8,10]
# target = 8

# Desired Output: 2


from collections import Counter

def target_from_list(num_list, target):
	# Creating the dictionary of the list.
	counter = Counter(num_list)

	# If the target exists in the list then the value in dictionary for that key is returned.
	if counter.__contains__(target):
		return(counter[target])


num_list = [5,7,7,8,8,10]
target = 8

occur = target_from_list(num_list,target)
print('Occurence of target %s is %s' %(target, occur))