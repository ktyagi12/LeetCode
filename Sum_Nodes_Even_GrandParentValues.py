#Problem available at: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return
        sum_ = 0
        stack = [(root,None,None)]
        
        while(stack):
            node,parent,grand_parent = stack.pop()
            if grand_parent and grand_parent.val%2 == 0:
                sum_ = sum_ + node.val
                
            if node.left:
                stack.append((node.left,node,parent))
            
            if node.right:
                stack.append((node.right,node,parent))

        return sum_
        