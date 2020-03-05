# Google Coding Interview Problem: 
# Given an input string S and two characters c1 and c2, you need to replace every occurence of character c1 with c2 in the given string. Do it recursively.

#  Input: 
# str : abba
# c1 = a
# c2 = x

# Desired Output: xbbx


# Iterative Approach
def char_replace_iter(str_, c1, c2):
	
	str_2 = ''

	for i in range(len(str_)):
		if str_[i] == c1:
			str_2  += c2
		else:
			str_2 += str_[i]
			

	return str_2


# Recursive Approach
def char_replace_rec(inval, c1, c2):
	
	if inval == '':
		return ''
	if inval[0] == c1:
		return c2 + char_replace_rec(inval[1:] , c1,c2)
	return inval[0] + char_replace_rec(inval[1:] , c1,c2)



str_ = input('\nEnter the input string..')

c1 = input('\nEnter the character to be replaced ?') 
c2 = input('\nEnter the character which will replace ?') 

str_2 = char_replace_iter(str_,c1,c2)
print('Output: ', str_2)


str_3 = char_replace_rec(str_,c1,c2)
print('Output: ', str_3)

