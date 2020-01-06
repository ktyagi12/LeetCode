#Problem available at: https://leetcode.com/problems/longest-common-prefix/submissions/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)!=0):
            long_prefix = []
            min_len = len(strs[0])

            for ele in strs:
                if len(ele) < min_len:
                    min_len = len(ele)

            strs = sorted(strs)
            shortest = strs[0]
            largest = strs[-1]        

            for i in range(min_len):

                if (len(largest) > i and shortest[i]==largest[i]):

                    long_prefix.append(shortest[i])

                else:

                    return "".join(long_prefix)

            return "".join(long_prefix)
        else:
            return ""