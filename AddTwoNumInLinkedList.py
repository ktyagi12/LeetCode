#Problem available at: https://leetcode.com/problems/add-two-numbers/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 or not l2:
            return
        
        dummy = ListNode(0)
        current = dummy
        carry = 0
       
        while(l1 or l2 or carry):
            if l1:
                carry = carry + l1.val
                l1 = l1.next
            
            if l2:
                carry = carry +l2.val
                l2 = l2.next
                
            current.next = ListNode(carry %10)
            current = current.next
            carry = carry // 10
        
        return dummy.next