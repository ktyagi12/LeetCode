#Problem available at: https://leetcode.com/problems/length-of-last-word/submissions/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        llist = s.split()
        return len(llist[-1]) if llist else 0
        