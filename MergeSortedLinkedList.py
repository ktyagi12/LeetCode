#Problem available at: https://leetcode.com/problems/merge-two-sorted-lists/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = l3 = ListNode(0)
        if(l1 == None and l2 == None):
            return None
        elif(l1 == None):
            return l2
        elif(l2 == None):
            return l1
        else:
            while(l1 and l2):
                if(l1.val < l2.val):
                    l3.next = l1
                    l1 = l1.next
                else:
                    l3.next = l2
                    l2 = l2.next
                
                l3 =l3.next
                    
            if(l1 == None):
                l3.next = l2 
            else:
                l3.next = l1 
        return cur.next