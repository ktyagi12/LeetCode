# Google Coding Interview Problem: 
# Given a string, compute recursively a new string where all the 'x' chars have been removed.


#  Input: xaxb


# Desired Output: ab


str_ = input('Enter the original string\n')
char_ = input('Enter the character to be removed\n')

str_out = ''

for i in str_:
	if i != char_:
		str_out += i

print('Output string after removal of %s is' %(char_))
print(str_out)

