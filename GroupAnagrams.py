#Problem available at:  https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if not strs:
            return
        result = []
        
        i = 0
        
        while(i < len(strs)):
            curr = strs[i]
            flattened_list = [item for items in result for item in items]
            
            if curr not in flattened_list:
                temp = [curr]
                for j in range(i+1, len(strs)):
                    curr_in = strs[j]
                    if len(curr_in) == len(curr):
                        c1 = Counter(curr_in)
                        c2 = Counter(curr)
                        
                        if c1 == c2:
                            temp.append(curr_in)
                            
                result.append(temp)
                
            i += 1
                
        return result


#====================================================================================

#Optimized Solution

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if not strs:
            return
        
        ans = collections.defaultdict(list)
        for i in strs:
            ans[tuple(sorted(i))].append(i)
        
        return ans.values()
