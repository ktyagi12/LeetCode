#Problem available at: https://leetcode.com/problems/remove-linked-list-elements/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
    
        start = head
        prev = None
        
        while(start):
            
            if start.val == val:
                
                if prev == None:
                    
                    head = head.next
                    start = head
                    
                elif start.next == None:
                    prev.next = None
                    break
                    
                else:
                    prev.next = start.next
                    start = start.next
                    
            else:
                prev = start
                start = start.next 
            
        return head
    
    