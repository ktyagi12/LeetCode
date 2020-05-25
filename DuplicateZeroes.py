# Problem available at: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/

# Question: Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        if not arr:
            return
        
        i = 0
        while(i < len(arr)):
            if arr[i] == 0:
                j = len(arr) - 1
                while(j > (i+1)):
                    arr[j] = arr[j-1]
                    j -= 1
                arr[j] = 0
                i += 2

            else:
                i += 1

        print(arr)