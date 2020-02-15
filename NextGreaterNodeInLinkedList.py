#Problem available at: https://leetcode.com/problems/next-greater-node-in-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return
        
        start = head
        llist = []
        
        while(start):
        
            llist.append(start.val)
            start = start.next
        
        
        for i in range(len(llist)-1):
            
            for j in range(i+1,len(llist)):
                if llist[j] > llist[i]:
                    llist[i] = llist[j]
                    break
            else:
                llist[i] = 0
        llist[-1] = 0          
                    
        print(llist)
        return llist

#=================================================================

#Problem available at: https://leetcode.com/problems/next-greater-node-in-linked-list/submissions/

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return
        
        start = head
        llist = []
        
        while(start):
        
            llist.append(start.val)
            start = start.next
        
        res = []
        
        for i in range(len(llist)-1,-1,-1):
            while res and res[-1] <= llist[i]:
                res.pop()
                
            res.append(llist[i])
            
            llist[i] = res[-2] if len(res) > 1 else 0
            
        return llist        