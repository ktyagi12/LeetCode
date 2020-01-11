#Problem available at: https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None:
            return 
        s = head
        n = s.next
        while(n != None):
            if s.val == n.val:
                s.next = n.next
                n = s.next
            else:
                s=s.next
                n=n.next
                
        return head