#Problem available at: https://leetcode.com/problems/symmetric-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root == None:
            return True
        if root.left == root.right == None:
            return True
        if root.left == None:
            return False
        if root.right == None:
            return False
        else:
            return self.checksymm(root.left,root.right)
    
            
        
    def checksymm(self,left,right):
        if left == right == None:
            return True
        if left == None or right == None:
            return False
        if left.val == right.val:
            return self.checksymm(left.left, right.right) and self.checksymm(left.right, right.left)
        else:
            return False
        