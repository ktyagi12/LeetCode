#Problem available at: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return 

        result = [0] * len(nums)            # Initializing the result with 0.
        #print(result)
        
        for i in range(len(nums)):          # Looping thro all the elements of the nums.
            
            count = 0                       # Counter for counting the numbers smaller than current number.
            
            for j in range(len(nums)):       
                
                if nums[i] > nums[j]:       # Checking if number is smaller than current number.
                    
                    count += 1              # Counting the numbers smaller than current number.
                    
                    result[i] = count       # Updating the count in the resultant list.
            
            #print('Result for {} is {}'.format(nums[i],result))         
        
        return result   


#=====================================================================================================================
# Optimized Solution

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return 

        result = [0] * len(nums)         
        temp = []
        
        for k,v in enumerate(nums):
            temp.append((k,v))
        
        temp.sort(reverse = True ,key=lambda x: x[1])
        
        
        for i in range(len(temp)):
            count = 0
            j = i+1
            flag = 1
            
            if i == len(temp)-1:
                result[temp[i][0]]= 0
                       
            elif(temp[i][1] == temp[j][1] and i <= len(temp)-1):       
               
                while(temp[i][1] == temp[j][1]):
                    
                    if (j == len(temp)-1):
                        
                        result[temp[i][0]] = 0
                        flag = 0
                        break
                        
                    else:
                        j += 1
                
                if flag == 1:
                    count = len(temp) - j
                       
            else:                            
                 count = len(temp) - (i+1)
                       
            result[temp[i][0]] = count
                       
        return result         