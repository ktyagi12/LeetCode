#Problem available at: https://leetcode.com/problems/occurrences-after-bigram/submissions/
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        if not text or not first or not second:
            return 
        
        ans = []
        tup = (first, second)
        #print('Tuple: ',tup)
        
        bigrams = [b for b in zip(text.split(" ")[:-1], text.split(" ")[1:])]
        #print('Bigrams: ',bigrams)
        
        for i in range(len(bigrams)):
            if tup == bigrams[i]:
                #print('Found tup:', tup)
                if i+1 < len(bigrams):
                    ans.append(bigrams[i+1][1])
                      
        return ans