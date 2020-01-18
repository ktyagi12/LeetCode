#Problem available at: https://leetcode.com/problems/linked-list-cycle/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return
        if head.next == None:
            return False
        
        start = head
        while(1):
            if start.next==None:
                return False
            if start.next.val=='NA':
                return True
            else:
                start.val= 'NA'
                start=start.next
        return False

#=================================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if not head:
            return
        
        if head.next == None:
            return False
        
        fast = slow = head

        while slow and fast and fast.next:
        
            slow = slow.next                # Step of 1
            fast = fast.next.next           # Setp of 2

            if slow is fast:                # Checking whether two pointers meet
                return True

        return False        