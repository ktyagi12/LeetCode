#Problem available at: https://leetcode.com/problems/odd-even-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if not head:
            return
        
        even_head = head.next
        odd = head
        even = even_head
        
        while(even and even.next):
            odd.next = even.next
            even.next = odd.next.next
            
            
            odd = odd.next
            even = even.next
            
        
        if even:
            even.next = None
            
        odd.next = even_head
        
        return head