#Problem available at: https://leetcode.com/problems/linked-list-components/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        
        if not head or not G:
            return
        
        start = head
        sum_ = 0
        
        while(start):
            if start.val in G:
                sum_ += 1
                
                while(start is not None and start.next is not None and start.next.val in G):
                    start = start.next
            
            start = start.next
                   
        return sum_