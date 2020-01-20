#Problem available at: https://leetcode.com/problems/reverse-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        
        p = None
        start = head
        n = start.next
        while(start != None and n != None):
            start.next = p
            p = start
            start = n
            n = n.next
         
        start.next = p
        head = start
        return head
            
            