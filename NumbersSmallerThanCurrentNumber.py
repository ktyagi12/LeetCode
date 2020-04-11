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


         