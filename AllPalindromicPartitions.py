# Problem available at: https://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/

def check_palindrome(str_, left, right):
	while(left < right):
		if str_[left] != str_[right]:
			return False

		left += 1
		right -= 1

	return True



def check_palindrome_partition(final_list, curr_list, start, end, input_str):
	if start >= end:
		final_list.append(curr_list.copy())
		return


	for i in range(start, end):
		if check_palindrome(input_str,start,i):
			curr_list.append(input_str[start: i+1])
			check_palindrome_partition(final_list, curr_list, i+1, end, input_str)

			curr_list.pop()


def all_palindrome(input_str):
	start = 0
	end = len(input_str)
	final_list = []
	curr_list = []

	check_palindrome_partition(final_list, curr_list, start, end, input_str)

	for i in range(len(final_list)):
		for j in range(len(final_list[i])):
			print(final_list[i][j], end = " ")


if __name__ == "__main__":
	input_str = input()
	all_palindrome(input_str)
