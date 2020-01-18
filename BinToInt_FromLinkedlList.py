#Problem available at: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return
        
        start = head
        s = ''
        while(start != None):
            s = s+ str(start.val)
            print(s)
            
            start = start.next
            
        return int(s,2)