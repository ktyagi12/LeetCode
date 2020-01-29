#Problem available at: https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if not headA or not headB:
            return
        else:
            l= dict()
            while headB:
                l[headB] = headB.next
                headB = headB.next
                
            while headA:
                if l.__contains__(headA):
                    return headA
                
                headA = headA.next