#Problem available at: https://leetcode.com/problems/unique-number-of-occurrences/submissions/
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        if not arr:
            return
        
        count = collections.Counter(arr)
        v = list(count[k] for k in count)

        uniq = set()
        
        for i in count.values():
            if i in uniq:
                return False
            else:
                uniq.add(i)
            
        return True
        
        