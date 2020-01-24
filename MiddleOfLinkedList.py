#Problem available at: https://leetcode.com/problems/middle-of-the-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return
        start = head
        cnt = 0
        while(start):
            cnt = cnt +1
            
            start = start.next
            
        if cnt%2 == 0:
            start = head
            mid = cnt //2
            while(mid > 0):
                start = start.next
                mid = mid - 1
            head = start
            return head
            
        else:
            start = head
            mid = cnt //2
            while(mid > 0):
                start = start.next
                mid = mid - 1
                
            head = start
            return head