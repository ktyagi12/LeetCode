# Google Coding Interview Problem: 
# Given a number n, put all the elements from 1 to n in an array in order 1,3,5.......4,2.

#  Input: 10

# Desired Output: [1,3,5,7,9,8,6,4,2]


n = int(input('Enter the number\n'))

out_odd = []
out_even = []

for i in range(1,n):
	if i % 2 == 1:
		out_odd.append(i)
	else:
		out_even.append(i)

# out_even.reverse()

out_even = out_even[::-1]

out_odd.extend(out_even)

print(out_odd)