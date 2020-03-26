#Problem :
## Given an array of N integers. Find the contiguous sub array with maximum sum.

num  = [1,2,3,-2,5]

max_ = 0
sum_ = 0

for i in range(len(num)):
	sum_ += num[i]

	if sum_ < 0:
		sum_ = 0
	elif sum_ > max_:
		max_ = sum_

print(max_)