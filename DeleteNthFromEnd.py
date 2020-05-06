# Problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

# Question: Given a linked list, remove the n-th node from the end of list and return its head.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        if not head or not n:
            return 0
        
        dummy = ListNode()
        dummy.next = head
        
        first = dummy
        second = dummy
        
        for i in range(n+1):
            first = first.next
            
        while(first != None):
            first = first.next
            second = second.next
            
        second.next = second.next.next
        return dummy.next