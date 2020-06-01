# Problem available at: https://www.geeksforgeeks.org/reverse-a-string-without-affecting-special-characters/

class ReverseString:

	def reverseString(self,input_str):
		curr_list = list(input_str)
		
		l = 0
		r = len(curr_list)-1

		while(l < r):
			if (not curr_list[l].isalpha()):
				l += 1
			elif (not curr_list[r].isalpha()):
				r -= 1
			else:
				curr_list[l], curr_list[r] = curr_list[r], curr_list[l]
				l += 1
				r -= 1
		
		input_str = ''.join(curr_list)

		return input_str


rev = ReverseString()
T = int(input())
for i in range(T):
	input_str = input()
	output_str = rev.reverseString(input_str)
	print(output_str)