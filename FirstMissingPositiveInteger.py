# Google Coding Interview Problem: 
# Given an unsorted integer array, find the first missing positive integer.

# TC: O(n)
# SC: O(1)

# Input: 
# [3,4,-1,1]

# Desired Output: 2


def find_pos_miss(input_):
    set_ = set()

    for i in range(1,len(input_)+1):
        set_.add(i)

    return(set_ - set(input_))



input_ = [3,4,-1,1,2,6]
pos = find_pos_miss(input_)
print('First Missing positive number : ', pos)