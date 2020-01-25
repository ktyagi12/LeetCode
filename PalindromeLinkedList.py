#Problem available at: https://leetcode.com/problems/palindrome-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head:
            return True
        
        llist = []
        
        start = head
        
        while(start):
            llist.append(start.val)
            start = start.next
            
        print(llist)
        llist1 = llist[::-1]
        #print(llist1)
        
        if llist == llist1:
            return True
        else:
            return False
        