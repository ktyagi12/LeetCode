# Google Coding Interview Problem: 
# Given a str_in, compute recursively a nw str_in where all appearences of "pi" have been replaced by "3.14".

#  Input: 
# str : xpix

# Desired Output: x3.14x

# Iterative Approach
def pi_replace_iter(str_in, str_out):
	
	i = 0
	
	while(i < len(str_in)):
		if str_in[i] == 'p' and str_in[i+1] == 'i':
			str_out += '3.14'
			i += 2
		else:
			str_out += str_in[i]
			i += 1
		
	return str_out


# Recursive Approach
def pi_replace_rec(llist,start):
	if len(llist) < 2 or start == len(llist): 
		return llist 

	pi_replace_rec(llist, start + 1) 

	if(llist[start] == 'p' and llist[start + 1] == 'i'): 
		llist[start:start + 2] = ['3', '.', '1', '4']
		print(llist)

str_in = input('\nEnter the input str_in..')

str_out = ''
str_iter = pi_replace_iter(str_in, str_out)

llist = list(str_in)
pi_replace_rec(llist,0)

llist = ''.join(llist)

print('Iterative Output: ', str_iter)
print('Recursive Output: ', llist)
